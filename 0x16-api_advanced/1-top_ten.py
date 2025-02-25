#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Set a custom User-Agent header
    headers = {"User-Agent": "MyRedditBot/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        # Parse the JSON response
        data = response.json()

        # Extract the first 10 hot posts
        posts = data["data"]["children"][:10]
        
        for post in posts:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)
