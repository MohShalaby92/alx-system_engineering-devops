#!/usr/bin/python3
"""
Queries the reddit API and returns the number of subscribers for a given subriddet.
if the subreddit is invalid, returns 0
"""

import requests

def number_of_subscribers(subreddit):

    headers = {"User-Agent": "MyRedditBot/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers-headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        data = response.json()

        subscribers = data["data"]["subscribers"]
        return subscribers
    except (KeyError, ValueError):
        return 0
