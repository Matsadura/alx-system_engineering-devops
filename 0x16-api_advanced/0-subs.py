#!/usr/bin/python3
"""Returns the number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    base_url = "https://oauth.reddit.com/"
    api_url = f"r/{subreddit}/about.json"

    try:
        response = requests.get(base_url + api_url)
        response = response.json()
        subscribers = response['data']['subscribers']
        return subscribers
    except Exception as E:
        return 0
