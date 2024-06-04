#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        total_subscribers = response.json().get('data').get('subscribers')
        print(total_subscribers)
    else:
        print(0)


if __name__ == "__main__":
    import requests
    from sys import argv

    subreddit = argv[1] if len(argv) > 1 else ''
    if not subreddit:
        print("Usage: {} <subreddit>".format(argv[0]))
        exit(1)

    number_of_subscribers(subreddit)
