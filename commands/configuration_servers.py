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
        channels = ctx.guild.channels
        progression = len(channels)
        total = 10
        task_finish = 1
        saving_embed =  discord.Embed(title="Sauvegarde du serveur", description="La sauvegarde est en cours", colour = discord.Colour.gold())
        saving_embed.set_author(name= f"{ctx.message.author.name}")
        saving_embed.add_field(name = "Enregistrement: ", value = f"<---------->", inline= False)
        try:
            connect.add_server(self.bot, server_id, server_name, owner_id, owner_name)
        except:
            await ctx.message.channel.send("Impossible de sauvegarder le serveur")
        msg = await ctx.message.channel.send(embed = saving_embed)
        
        for channel in channels:
            progress_bar = "<"
            connect.add_channels(self.bot, ctx.guild.id, channel.name, str(channel.type), str(channel.category))
            for i in range (int(total*(task_finish / progression))):
                progress_bar = progress_bar + "="
            for y in range (10 - int(total*(task_finish / progression))):
                progress_bar = progress_bar + "-"
            progress_bar = progress_bar + ">"
            updated_embed =  discord.Embed(title= "Sauvegarde du serveur", description= "Sauvegarde en cours", colour = discord.Colour.gold())
            updated_embed.set_author(name= f"{ctx.message.author.name}")
            updated_embed.add_field(name = "Enregistrement: ", value = f"{progress_bar} {int(100*(task_finish / progression))}%", inline= False)
            await msg.edit(embed = updated_embed)
            task_finish = task_finish + 1
        updated_embed =  discord.Embed(title= "Sauvegarde du serveur", description= "Sauvegarde terminée", colour = discord.Colour.gold())
        updated_embed.set_author(name= f"{ctx.message.author.name}")
        updated_embed.add_field(name = "Enregistrement: ", value = f"{progress_bar} 100%", inline= False)
        await msg.edit(embed = updated_embed)

        print("terminé") 

def setup(client):
    client.add_cog(Configuration(client))
