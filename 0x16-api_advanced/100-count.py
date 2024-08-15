#!/usr/bin/python3
"""Function to tally occurrences of specified words in hot posts from a given Reddit subreddit."""
import requests


def count_keywords(subreddit, keywords, word_counts={}, next_page="", total_count=0):
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    query_params = {
        "after": next_page,
        "count": total_count,
        "limit": 100
    }
    response = requests.get(api_url,
                            headers=request_headers,
                            params=query_params,
                            allow_redirects=False)

    try:
        response_data = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    post_data = response_data.get("data")
    next_page = post_data.get("after")
    total_count += post_data.get("dist")

    for post in post_data.get("children"):
        title_words = post.get("data").get("title").lower().split()
        for keyword in keywords:
            if keyword.lower() in title_words:
                occurrences = len([word for word in title_words if word == keyword.lower()])
                if word_counts.get(keyword) is None:
                    word_counts[keyword] = occurrences
                else:
                    word_counts[keyword] += occurrences

    if next_page is None:
        if len(word_counts) == 0:
            print("")
            return
        sorted_word_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
        [print("{}: {}".format(word, count)) for word, count in sorted_word_counts]
    else:
        count_keywords(subreddit, keywords, word_counts, next_page, total_count)
