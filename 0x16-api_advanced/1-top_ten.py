#!/usr/bin/python3
"""
queries the reddit API and prints the titles of the first 10 hot posts for a given subreddit.
if the subreddit is invalid, prints None.
"""

def top_ten(subreddit):

    headers = {"User-Agent": "MyRedditBot/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = response.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()

        posts = data["data"]["children"][:10]

        for post in posts:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)

    
