import discord
import asyncio
import time
import asyncpg
from discord.ext import tasks, commands
from itertools import cycle

client = commands.Bot(command_prefix = 'e/')

@client.event
async def on_ready(): 
    print('Bot is ready')
    await client.change_presence(status=discord.Status.idle, activity= discord.Game("with the API"))



@client.event
async def on_member_join(member):
    print(f'{member} à rejoint le serveur')

@client.event
async def on_member_remove(member):
    print(f'{member} à quitté le serveur')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def test(ctx):
    guilds_channels = ctx.guild.channels
    for channel in guilds_channels:
        print(f"Le channel {channel.name} est un {channel.type}")


client.run('')