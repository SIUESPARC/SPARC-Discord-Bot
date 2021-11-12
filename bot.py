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

def send_groupme(message: discord.message.Message) -> None:
    """
    Receive a discord message and send a post request with it to GroupMe
    """

    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : GROUPME,
        'text' : message.content,
        }
    r = requests.post(url, json=data)
    print(r.status_code, r.reason)

def sanitize(message: discord.message.Message) -> discord.message.Message:
    """
    Un-Discordize the message by removing any channel or role tags to 
    make the message readable in GroupMe
    """
    message.content = message.content.replace
    return message

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
    else:
        print("Invalid Channel")
        await message.channel.send(message.content)

client.run(TOKEN)