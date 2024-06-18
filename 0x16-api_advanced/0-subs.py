#!/usr/bin/python3
"""Returns the number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    base_url = "https://api.reddit.com/"
    api_url = f"r/{subreddit}/about"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(base_url + api_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    response = response.json()
    if 'dist' in response['data'].keys():
        return 0
    return response['data']['subscribers']
