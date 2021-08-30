# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    print(f'{member.name} has joined the Discord server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'{message.author} has sent a message in the discord')

client.run(TOKEN)
