#!/usr/bin/python3
"""Returns the number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    base_url = "https://oauth.reddit.com/"
    api_url = f"r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        response = requests.get(base_url + api_url, headers=headers)
        response = response.json()
        subscribers = response['data']['subscribers']
        return subscribers
    except Exception as E:
        return 0
