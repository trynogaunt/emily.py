import discord
import asyncio
from discord.ext import commands
import functions.connection as connect
import functions.load_config as config 

class Configuration(commands.Cog, name="Configuration"):
    def __init__(self, client):
        self.client = client
        self.bot = config.BotConfig()

    @commands.command()
    async def save_server(self, ctx):
        server_id = ctx.message.guild.id
        server_name = ctx.message.guild.name
        owner_name = ctx.message.guild.owner.name
        owner_id = ctx.message.guild.owner_id
        try:
            connect.add_server(self.bot, server_id, server_name, owner_id, owner_name)
            await ctx.message.channel.send("Serveur sauvegardé")
        except NameError:
            await ctx.message.channel.send("Impossible de sauvegarder le serveur")
    
    @commands.command()
    async def save_channel(self, ctx):
        for channel in ctx.guild.channels:
            await ctx.message.channel.send(f"{channel.name} est un {channel.type}, placé dans {channel.category}")
        
def setup(client):
    client.add_cog(Configuration(client))
