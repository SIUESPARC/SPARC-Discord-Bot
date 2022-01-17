# bot.py
import os
import requests

import discord
from discord.ext import commands
import tweepy
from dotenv import load_dotenv

from integrations import send_groupme, tweet

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
        send_groupme(GROUPME, message)
        tweet(twitter_client, message)

    await bot.process_commands(message)

# Commands
@bot.command(name="ping", pass_context=True)
async def calendar(ctx):
    await ctx.send('pong')

@bot.command(name="playing", pass_context=True)
async def playing(ctx, game):
    await bot.change_presence(activity = discord.Game(game))

@bot.command(name='kanye')
async def kanye(ctx):
    url = "https://api.kanye.rest/"
    response = requests.get(url)
    quote = response.json()['quote']
    await ctx.send(quote)

if __name__ == "__main__":
    bot.run(TOKEN)

