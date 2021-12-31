# bot.py
import os

import requests


import discord
from dotenv import load_dotenv


# Get necessary credentials from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GROUPME = os.getenv('GROUPME_BOT_ID')
CHANNELS = os.getenv('CHANNELS')        # CHANNELS will hold a list of 
                                        # channel ids 

client = discord.Client()

def send_groupme(message: str) -> None:
    """Receive a message and copy message into groupMe

    Args:
        message (str): Message to be sent to GroupMe
    """

    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : GROUPME,
        'text' : message,
        }
    r = requests.post(url, json=data)
    print(r.status_code, r.reason)

def tweet(message: str) -> None:
    """Receive a message and tweet message to Twitter account

    Args:
        message (str): Message to be tweeted
    """
    pass

def sanitize(message: discord.message.Message) -> str:
    """Un-Discordize the message by removing any channel or role tags to 
    make the message readable in GroupMe

    Args:
        message (discord.message.Message): Discord Message with tags

    Returns:
        str: Message with discord tags converted to text
    """
    print(f"Message before: {message.content}")

    sanitized = f"{message.author.display_name}: {message.clean_content}"

    return sanitized


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if str(message.channel.id) in CHANNELS:
        message = sanitize(message)
        send_groupme(message)

client.run(TOKEN)

