import requests
from pprint import pprint

import tweepy

def send_groupme(bot_id: str, message: str) -> None:
    """Receive a message and copy message into groupMe

    Args:
        message (str): Message to be sent to GroupMe
    """

    url = 'https://api.groupme.com/v3/bots/post'
    message = f"{message.author.display_name}: {message.clean_content}"
    data = {
        'bot_id' : bot_id,
        'text' : message,
        }
    r = requests.post(url, json=data)
    print(f"GroupMe Status: {r.status_code}, {r.reason}")

def tweet(client: tweepy.Client, message: str) -> None:
    """Receive a message and tweet message to Twitter account

    Args:
        message (str): Message to be tweeted
    """
    message = message.clean_content
    response = client.create_tweet(text=message)
    pprint(f"Tweet Status: {response}")

