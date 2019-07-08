import discord
import asyncio
import time
import asyncpg
from discord.ext import tasks, commands
import functions.database as d
import random
import functions.load_config as c

client = commands.Bot(command_prefix = c.prefix)
client.remove_command('help')
embed_img =['https://cdn.discordapp.com/attachments/556807734436167710/587636780694503436/hk416_girls_frontline_drawn_by_nlitz__b548fd4deda227586ab681f3aeef700c.png','https://cdn.discordapp.com/attachments/556807734436167710/583731618280112129/IMG_20190530_205301.jpg','https://cdn.discordapp.com/attachments/556807734436167710/587592676526915594/a2ZrZ7e_700b.png', ' https://cdn.discordapp.com/attachments/556807734436167710/580066744907857925/IMG_20190520_181410.jpg']

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

@client.command(name= "ping", description = "Plus c'est haut plus t'es retardé")
async def ping(ctx):
    ping = int(client.latency * 100)
    user_avatar = ctx.message.author.avatar_url
    ping_embed = discord.Embed(title = "PONG :ping_pong:", description = f"{ping}ms mon pote, too fast" , colour = discord.Colour.purple())
    ping_embed.set_thumbnail(url= user_avatar)
    ping_embed.set_footer(text="I'm Tryno's waifu but I'm your Bot")
    await ctx.channel.purge(limit= 1)
    await ctx.message.channel.send(embed = ping_embed)

@client.command(pass_context = True , name = "help", description = "T'envoie mon aide")
async def help(ctx, *help_type):
    user_avatar = ctx.message.author.avatar_url
    help_embed = discord.Embed(title = "Voici mon aide", description = "Bonjour je suis Emily", colour = discord.Colour.green())
    help_embed.set_thumbnail(url= random.choice(embed_img))
    help_embed.set_footer(text="I'm Tryno's waifu but I'm your Bot")
    help_embed.set_author(name = f"{ctx.message.author.name}", icon_url = f"{user_avatar}" )

    for command in client.commands:
        help_embed.add_field(name = command.name , value = command.description, inline= False)

    await ctx.channel.purge(limit= 1)
    await ctx.message.channel.send(embed = help_embed)

@client.command(name = "clear", description = "Permet supprimer des messages", type = "administration")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command(name = "configserver", description="Sauvegarde la configuration du serveur discord")
async def configserver(ctx, password):
    d.setup_server(ctx, password)
    await ctx.channel.purge(limit= 1)
    await ctx.message.channel.send("La configuration du serveur a bien était enregistrée")


@client.command(name = "deleteserver", description = "Suprimme la sauvegarde du serveur")
async def deleteserver(ctx, password):
   deleting = d.delete_server(ctx, password)
   if deleting == False:
       msg = "Votre serveur n'est pas sauvegardé ou votre mot de passe est incorrect"
   else:
       msg = "Configuration supprimée"
       await ctx.message.channel.send("La configuration du serveur va disparaitre")
       await asyncio.sleep(5)
   await ctx.channel.purge(limit= 1)
   await ctx.message.channel.send(msg)



@client.command(name = "rewriteserver", description = "Recréé le serveur à partir de sa sauvegarde")
async def rewriteserver(ctx, password):
    rewriting =  d.rewrite_server(ctx, password)
    if rewriting == False:
        await ctx.message.channel.send("Votre serveur n'est pas sauvegardé ou votre mot de passe est incrorrect")
    else:
        await ctx.channel.purge(limit= 1)
        for x in rewriting:
            channel_name, channel_type = x
            channel_name = channel_name.decode("utf-8")
            channel_type = channel_type.decode("utf-8")
            if channel_type == "voice":
                await ctx.guild.create_voice_channel(channel_name)
            elif channel_type == "text":
                await ctx.guild.create_text_channel(channel_name)

    

client.run(c.bot_token)