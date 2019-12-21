import discord
import asyncio
from discord.ext import commands
import random
import functions.load_config as c

class Tools(commands.Cog, name="tools"):
    def __init__(self, client):
        self.client = client
        self.bot = c.BotConfig()
        self.embed_img =['https://cdn.discordapp.com/attachments/556807734436167710/587636780694503436/hk416_girls_frontline_drawn_by_nlitz__b548fd4deda227586ab681f3aeef700c.png','https://cdn.discordapp.com/attachments/556807734436167710/583731618280112129/IMG_20190530_205301.jpg','https://cdn.discordapp.com/attachments/556807734436167710/587592676526915594/a2ZrZ7e_700b.png', ' https://cdn.discordapp.com/attachments/556807734436167710/580066744907857925/IMG_20190520_181410.jpg']
        self.not_see_command = self.bot.no_help
        
    @commands.command(pass_context = True , name = "help", description = "T'envoie mon aide")
    async def help(self, ctx, *help_type):
        user_avatar = ctx.message.author.avatar_url
        help_embed = discord.Embed(title = "Voici mon aide", description = "Bonjour je suis Emily", colour = discord.Colour.green())
        help_embed.set_thumbnail(url= random.choice(self.embed_img))
        help_embed.set_footer(text="I'm Tryno's waifu but I'm your Bot")
        help_embed.set_author(name = f"{ctx.message.author.name}", icon_url = f"{user_avatar}" )
        for command in self.client.commands:

            if command.name not in self.bot.no_help:
             help_embed.add_field(name = command.name , value = command.description, inline= False)
             
        help_embed.add_field(name = "Mon support:", value = "https://discord.gg/abdd2sk", inline = False)
        await ctx.channel.purge(limit= 1)
        await ctx.message.channel.send(embed= help_embed)

    @commands.command(name= "ping", description = "Indique la latence du bot")
    async def ping(self, ctx):
        ping = int(self.client.latency * 100)
        user_avatar = ctx.message.author.avatar_url
        ping_embed = discord.Embed(title = "PONG :ping_pong:", description = f"{ping}ms mon pote, too fast" , colour = discord.Colour.purple())
        ping_embed.set_thumbnail(url= user_avatar)
        ping_embed.set_footer(text="I'm Tryno's waifu but I'm your Bot")
        await ctx.channel.purge(limit= 1)
        await ctx.message.channel.send(embed = ping_embed)

    @commands.command(name = "clear", description = "Permet supprimer des messages")
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=5):
        try:
            if amount < 100: 
                await ctx.channel.purge(limit= amount + 1)
            else: 
                await ctx.message.channel.send(f"Une erreur est survenue")
        except Exception as error:
            await ctx.channel.purge(limit= 1)
            await ctx.message.channel.send(f"Une erreur est survenue {error}")

def setup(client):
    client.add_cog(Tools(client))