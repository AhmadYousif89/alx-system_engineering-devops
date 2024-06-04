#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        total_subscribers = response.json().get('data').get('subscribers')
        return total_subscribers
    else:
        return 0


if __name__ == "__main__":
    from sys import argv

    subreddit = argv[1] if len(argv) > 1 else ''
    if not subreddit:
        print("Usage: {} <subreddit>".format(argv[0]))
        exit(1)

    number_of_subscribers(subreddit)
