import discord
import asyncio
import time
import asyncpg
from discord.ext import tasks, commands
import functions.database as d
import random
import functions.load_config as c

client = commands.Bot(command_prefix = c.prefix)
extensions = ['commands.configuration_servers', 'commands.tools']

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f"{extension} a bien était chargée")
        except Exception as error:
            print(f"{extension} ne peut pas être chargée, {error}")

@client.event
async def on_ready(): 
    print('Bot is ready')
    await client.change_presence(status=discord.Status.online, activity= discord.Game("e/help"))

@client.event
async def on_member_join(member):
    print(f'{member} à rejoint le serveur')

@client.event
async def on_member_remove(member):
    print(f'{member} à quitté le serveur')

client.run(c.bot_token)