#!/usr/bin/python3
""" 0-subs Module
"""
import requests


def number_of_subscribers(subreddit):
    """ This function return the number of subscibers of a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'Custom User Agent'})

    if response.status_code != 200:
        return 0

    user_info = response.json()

    return user_info['data']['subscribers']
