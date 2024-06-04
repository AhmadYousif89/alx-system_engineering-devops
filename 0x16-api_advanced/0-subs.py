#!/usr/bin/python3

"""This module contains number_of_subscribers functions"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
