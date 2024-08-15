#!/usr/bin/python3
"""
Defines a function to display the top
hot posts from a specified Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Displays the titles of the top 10
    hottest posts on the specified subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(url,
                            headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")

    [print(cr.get("data").get("title")) for cr in results.get("children")]
