#!/usr/bin/python3
"""
Query the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code > 399:
        return None
    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '')
        hot_list.append(title)
    after = response.json().get('data', {}).get('after', None)
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
