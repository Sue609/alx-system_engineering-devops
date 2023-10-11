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
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    elif response.status_code == 404:
        print(None)
        return
