#!/usr/bin/python3
"""
This module introduces a function.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
