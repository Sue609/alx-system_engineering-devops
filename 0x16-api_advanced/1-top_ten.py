#!/usr/bin/python3
"""
Module that introduces a function.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries and prints the titles of the first 10 hot posts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    elif response.status_code == 404:
        print(None)
        return
