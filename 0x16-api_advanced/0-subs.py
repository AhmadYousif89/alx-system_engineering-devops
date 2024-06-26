#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 Chrome/125.0.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code > 399:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
