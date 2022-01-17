# bot.py
import os
import requests
from pprint import pprint

import discord
from discord.ext import commands
import tweepy
from dotenv import load_dotenv

# Get discord and GroupMe credentials
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GROUPME = os.getenv('GROUPME_BOT_ID')
CHANNELS = os.getenv('DISCORD_CHANNELS')        # CHANNELS will hold a list of channel ids 

# Get twitter credentials
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate and connect to twitter API
twitter_client = tweepy.Client( consumer_key=CONSUMER_KEY,
                                consumer_secret=CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                access_token_secret=ACCESS_TOKEN_SECRET)

bot = commands.Bot(command_prefix='!')

def send_groupme(message: str) -> None:
    """Receive a message and copy message into groupMe

    Args:
        message (str): Message to be sent to GroupMe
    """

    url = 'https://api.groupme.com/v3/bots/post'
    message = f"{message.author.display_name}: {message.clean_content}"
    data = {
        'bot_id' : GROUPME,
        'text' : message,
        }
    r = requests.post(url, json=data)
    print(f"GroupMe Status: {r.status_code}, {r.reason}")

def tweet(message: str) -> None:
    """Receive a message and tweet message to Twitter account

    Args:
        message (str): Message to be tweeted
    """
    message = message.clean_content
    response = twitter_client.create_tweet(text=message)
    pprint(f"Tweet Status: {response}")



# Events
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity = discord.Game('Minecraft'))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if str(message.channel.id) in CHANNELS:
        send_groupme(message)
        tweet(message)

    await bot.process_commands(message)

# Commands
@bot.command(name="ping", pass_context=True)
async def calendar(ctx):
    await ctx.send('pong')

@bot.command(name="playing", pass_context=True)
async def playing(ctx, game):
    await bot.change_presence(activity = discord.Game(game))

if __name__ == "__main__":
    bot.run(TOKEN)

