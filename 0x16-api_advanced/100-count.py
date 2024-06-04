#!/usr/bin/python3
"""
Query the Reddit API and parses the title of all hot articles,
and prints a sorted count of given keywords 
"""
import requests


def count_words(subreddit, word_list, word_dict={}, after=None):
    """Count words in titles of hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        children = response.json().get('data').get('children')
        for child in children:
            title = child.get('data').get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        after = response.json().get('after')
        if after:
            return count_words(subreddit, word_list, word_dict, after)
        sorted_dict = sorted(
            word_dict.items(), key=lambda x: x[1], reverse=True
        )
        for k, v in sorted_dict:
            print("{}: {}".format(k, v))
    except Exception:
        return
