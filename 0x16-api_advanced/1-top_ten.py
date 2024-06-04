#!/usr/bin/python3
"""
Query the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code > 399:
        print(None)
        return
    posts = response.json().get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post.get('data', {}).get('title', ''))
