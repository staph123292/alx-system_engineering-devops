#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    # Set the URL to query the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom headers with a User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response to get the number of subscribers
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If the subreddit is invalid or another error occurred, return 0
            return 0
    
    except requests.RequestException as e:
        # If any exception occurs during the request, return 0
        return 0
