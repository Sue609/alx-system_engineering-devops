#!/usr/bin/python3
"""
This module introduces a function that returns number of subs.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that returns the number of subscribers for a given redit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    elif response.status_code == 404:
        return 0

    else:
        return 0
