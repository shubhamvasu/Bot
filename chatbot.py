import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print('Thank you..!!')
    await client.change_presence(game=discord.Game(name='videos'))

@client.event
async def on_message(message):
    if message.content.startwith('.hello'):
        msg = 'Hello {O.author.mention} How are you today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startwith('.bye'):
        msg = 'Goodbye {O.author.mention} will see you again soon :wave:'.format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
