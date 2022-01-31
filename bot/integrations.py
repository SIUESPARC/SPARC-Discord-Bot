import requests
import os
from pprint import pprint

import tweepy

def send_groupme(bot_id: str, message: str) -> None:
    """Receive a message and copy message into groupMe

    Args:
        message (str): Message to be sent to GroupMe
    """
    def send_message(bot_id: str, message: str) -> None:
        """Send a message to GroupMe

        Args:
            bot_id (str): GroupMe bot id
            message (str): Message to be sent to GroupMe
        """
        url = f"https://api.groupme.com/v3/bots/post"
        data = {
            "bot_id": bot_id,
            "text": message
        }
        r = requests.post(url, json=data)
        print(f"GroupMe Status: {r.status_code}, {r.reason}")


    message = f"{message.author.display_name}: {message.clean_content}"

    while len(message) > 1000:
        sliced_message = message[:1000]
        slice_index = sliced_message.rfind('\n\n')
        message_to_send = sliced_message[:slice_index]
        message = message[slice_index:]

        send_message(bot_id, message_to_send)
    
    send_message(bot_id, message)


def tweet(client: tweepy.Client, message: str) -> None:
    """Receive a message and tweet message to Twitter account

    Args:
        message (str): Message to be tweeted
    """
    message = message.clean_content
    response = client.create_tweet(text=message)
    pprint(f"Tweet Status: {response}")