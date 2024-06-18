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
    response = requests.get(base_url + api_url, headers=headers)
    if response.status_code != 200:
        return 0
    response = response.json()
    if 'dist' in response['data'].keys():
        return 0
    return response['data']['subscribers']
