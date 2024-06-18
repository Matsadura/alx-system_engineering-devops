#!/usr/bin/python3
"""Contains the top_ten function"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10
    hot posts listed for a given subreddit"""
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    headers = {'User-Agent': 'MyClient/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        exit()
    subreddits = response.json()
    children = subreddits['data']['children']
    [print(children[i]['data']['title']) for i in range(10)]
