#!/usr/bin/python3
"""
Function to count words in all
hot posts of a given Reddit subreddit.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after="", word_count=Counter()):
    """
    Recursively queries the Reddit API,
    parses titles of hot articles, and counts
    the occurrences
    of specified keywords (case-insensitive).

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): The after parameter for pagination
        in the Reddit API.
        word_count (Counter): A Counter object to
        store keyword counts.

    Returns:
        None: The function prints the sorted count of keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url,
                            headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return

    data = response.json().get("data", {})
    after = data.get("after")

    word_list = [word.lower() for word in word_list]

    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower()
        for word in word_list:
            word_count[word] += title.split().count(word)

    if after:
        return count_words(subreddit, word_list, after, word_count)

    if word_count:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda item:
                                   (-item[1], item[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
