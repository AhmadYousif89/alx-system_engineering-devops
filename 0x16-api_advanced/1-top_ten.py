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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code > 399:
        print(None)
        return
    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title', ''))
