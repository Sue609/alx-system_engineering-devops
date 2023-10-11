#!/usr/bin/python3
"""
This module introduces a function.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries and counts occurrences of
    keywords in hot article titles.
    """
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            title = post['data']['title'].lower()
            for keyword in word_list:
                if keyword.lower() in title:
                    keyword_lower = keyword.lower()
                    counts[keyword_lower] = counts.get(keyword_lower, 0) + 1
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword.lower()}: {count}")
    elif response.status_code == 404:
        return
