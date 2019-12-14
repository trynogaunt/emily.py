import discord
import asyncio
from discord.ext import commands
import functions.connection as connect
import functions.load_config as config 

class Configuration(commands.Cog, name="Configuration"):
    def __init__(self, client):
        self.client = client
        self.bot = config.BotConfig()
        self.database = connect.database_connection(self.bot)

    @commands.command()
    async def save_server(self):
        print("test")
        
def setup(client):
    client.add_cog(Configuration(client))
