import discord
import asyncio
from discord.ext import commands
import random
import functions.load_config as c
import functions.connection as connect

class Configuration(commands.Cog, name="configuration"):
    def __init__(self, client):
        self.client = client
        self.bot = c.BotConfig()

    @commands.command(pass_context = True , name = "save_server", description = "Sauvegarde le serveur")
    async def save_server(self, ctx):
        server_id = ctx.message.guild.id
        server_name = ctx.message.guild.name

        owner_name = ctx.message.guild.owner.name
        owner_id = ctx.message.guild.owner_id

        channels = ctx.guild.channels
        load_channel = len(channels)
        channel_finish = 1

        members = ctx.guild.members
        load_member = len(members)
        member_finish = 1

        roles = ctx.guild.roles
        load_role = len(roles)
        role_finish = 1

        total = 10
        
        saving_embed =  discord.Embed(title="Sauvegarde du serveur", description="La sauvegarde est en cours", colour = discord.Colour.gold())
        saving_embed.set_author(name= f"{ctx.message.author.name}")
        saving_embed.add_field(name = "Channels ", value = f"<---------->", inline= False)
        saving_embed.add_field(name = "Rôles", value = f"<---------->", inline= False)

       
        connect.add_server(self.bot, server_id, server_name, owner_id, owner_name)
        msg = await ctx.message.channel.send(embed = saving_embed)
        
        for channel in channels: #enregistrement de tout les channels
            progress_bar = "<"
            connect.add_channels(self.bot, ctx.guild.id, channel.name, str(channel.type), str(channel.category))
            for i in range (int(total*(channel_finish / load_channel))):
                progress_bar = progress_bar + "="
            for y in range (10 - int(total*(channel_finish / load_channel))):
                progress_bar = progress_bar + "-"
            progress_bar = progress_bar + ">"
            updated_embed =  discord.Embed(title= "Sauvegarde du serveur", description= "Sauvegarde en cours", colour = discord.Colour.gold())
            updated_embed.set_author(name= f"{ctx.message.author.name}")
            updated_embed.add_field(name = "Channels: ", value = f"{progress_bar} {int(100*(channel_finish / load_channel))}%", inline= False)
            updated_embed.add_field(name = "Rôles:", value = f"<---------->", inline= False)
            updated_embed.add_field(name = "Membres:", value = f"<---------->", inline= False)
            await msg.edit(embed = updated_embed)
            channel_finish = channel_finish + 1
            
        for role in roles: #enregistrement de tous les rôles
            progress_bar = "<"
            connect.add_roles(self.bot, role.name, str(role.colour.to_rgb()), role.hoist, role.mentionable, role.id, role.position)
            for i in range(int(total*(role_finish / load_role))):
                progress_bar = progress_bar + "="
            for y in range (10 - int(total*(role_finish / load_role))):
                progress_bar = progress_bar + "-"
            progress_bar = progress_bar + ">"
            updated_embed =  discord.Embed(title= "Sauvegarde du serveur", description= "Sauvegarde en cours", colour = discord.Colour.gold())
            updated_embed.set_author(name= f"{ctx.message.author.name}")
            updated_embed.add_field(name = "Channels: ", value = f"<==========> 100%", inline= False)
            updated_embed.add_field(name = "Rôles:", value = f"{progress_bar} {int(100*(role_finish / load_role))}%", inline= False)
            updated_embed.add_field(name = "Membres:", value = f"<---------->", inline= False)
            await msg.edit(embed = updated_embed)
            role_finish = role_finish + 1

        for member in members: #enregistrement de tous les membres
            progress_bar = "<"
            try:
                connect.add_members(self.bot, member.id, member.name, server_id)
            except:
                print(f"{member.name} est déjà enregistré")
                pass
            for i in range(int(total*(member_finish / load_member))):
                progress_bar = progress_bar + "="
            for y in range (10 - int(total*(member_finish / load_member))):
                progress_bar = progress_bar + "-"
            progress_bar = progress_bar + ">"
            updated_embed =  discord.Embed(title= "Sauvegarde du serveur", description= "Sauvegarde en cours", colour = discord.Colour.gold())
            updated_embed.set_author(name= f"{ctx.message.author.name}")
            updated_embed.add_field(name = "Channels: ", value = f"<==========> 100%", inline= False)
            updated_embed.add_field(name = "Rôles:", value = f"<==========> 100%", inline= False)
            updated_embed.add_field(name = "Membres:", value = f"{progress_bar} {int(100*(member_finish / load_member))}%", inline= False)
            await msg.edit(embed = updated_embed)
            member_finish = member_finish + 1

def setup(client):
    client.add_cog(Configuration(client))