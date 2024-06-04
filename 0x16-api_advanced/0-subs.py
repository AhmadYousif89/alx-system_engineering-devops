#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code > 399:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)


if __name__ == "__main__":
    from sys import argv

    subreddit = argv[1] if len(argv) > 1 else ''
    number_of_subscribers(subreddit)
