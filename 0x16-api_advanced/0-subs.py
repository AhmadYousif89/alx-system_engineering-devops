#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    if not subreddit:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    total_subscribers = response.json().get('data', {}).get('subscribers', 0)
    return total_subscribers


if __name__ == "__main__":
    from sys import argv

    subreddit = argv[1] if len(argv) > 1 else ''
    number_of_subscribers(subreddit)
