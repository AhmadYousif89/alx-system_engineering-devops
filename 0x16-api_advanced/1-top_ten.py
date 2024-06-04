#!/usr/bin/python3
"""
Query the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url, allow_redirects=False)
    if response.status_code > 399:
        print(None)
        return
    for post in response.json().get('data', {}).get('children', []):
        print(post.get('data', {}).get('title', ''))
