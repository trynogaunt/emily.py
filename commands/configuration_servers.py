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
        msg = await ctx.message.channel.send(f"Enregistrement: <---------->")
        channels = ctx.guild.channels
        for channel in channels:
            connect.add_channels(self.bot, ctx.guild.id, channel.name, str(channel.type), str(channel.category))
            await msg.edit(content = f"Enregistrement de {channel.name}")
        await msg.edit(content = f"Enregistrement terminé")
        print("terminé")    
def setup(client):
    client.add_cog(Configuration(client))
