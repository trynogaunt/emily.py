import discord
import asyncio
from discord.ext import commands
import functions.database as d 

class Configuration(commands.Cog, name="Configuration"):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "configserver", description="Sauvegarde la configuration du serveur discord", visibilty = True)
    async def configserver(self,ctx, password):
        d.setup_server(ctx, password)
        await ctx.channel.purge(limit= 1)
        await ctx.message.channel.send("La configuration du serveur a bien était enregistrée")

    @commands.command(name = "deleteserver", description = "Supprime la sauvegarde du serveur", visibilty = True)
    async def deleteserver(self, ctx, password):
        deleting = d.delete_server(ctx, password)
        if deleting == False:
            msg = "Votre serveur n'est pas sauvegardé ou votre mot de passe est incorrect"
        else:
            msg = "Configuration supprimée"
        await ctx.message.channel.send("La configuration du serveur va disparaitre")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit= 1)
        await ctx.message.channel.send(msg)

    @commands.command(name = "rewriteserver", description = "Recréé le serveur à partir de sa sauvegarde", visibilty = True)
    async def rewriteserver(self, ctx, password):
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

def setup(client):
    client.add_cog(Configuration(client))
