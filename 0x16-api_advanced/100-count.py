#!/usr/bin/python3
"""
Query the Reddit API and parses the title of all hot articles,
and prints a sorted count of given keywords 
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code > 399:
        return None
    data = response.json().get('data', {})
    childs = data.get('children', [])
    for post in childs:
        title = post["data"]["title"]
        hot_list.append(title)
    after = data.get('after', None)
    if after:
        count_words(subreddit, word_list, hot_list, after)
    else:
        word_dict = {}
        for word in word_list:
            word_dict[word] = 0
        for title in hot_list:
            for word in word_list:
                word_dict[word] += title.lower().split(' ').count(word.lower())
        for k, v in sorted(word_dict.items(), key=lambda w: (-w[1], w[0])):
            if v > 0:
                print("{}: {}".format(k, v))
