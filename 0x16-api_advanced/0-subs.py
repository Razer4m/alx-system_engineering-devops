#!/usr/bin/python3
"""
Defines a function to retrieve the
number of subscribers for a specified Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves and returns the total number of
    subscribers for a specific subreddit.

    Args:
        subreddit (str): The name of the s

    Returns:
        int: The number of subscribers for the
        subreddit. Returns 0 if the
        subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")

    return results.get("subscribers")
