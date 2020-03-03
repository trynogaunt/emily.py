import discord
import asyncio
from discord.ext import commands
import functions.battleboard_config as battle
import functions.load_config as c

class Battle(commands.Cog, name="battle"):
    def __init__(self, client):
        self.client = client
        self.bot = c.BotConfig()

    @commands.command(pass_context = True , name = "start_battle", description = "test")
    async def start_battle(self, ctx, opponent : discord.Member):
        await ctx.message.channel.purge(limit = 1)
        await ctx.message.channel.send(f"{ctx.message.author.mention} lance un défi à {opponent.mention}")
        channel = await opponent.create_dm()
        game = battle.create_game(ctx.message.author, opponent)
        print(f"Joueur 1: {game.player_one.name}\nPlateau:\n" + game.player_one.print_board() + "\nSa vue:\n" + game.player_one.print_view()+ f"\nJoueur 2: {game.player_two.name}\nPlateau:\n" + game.player_two.print_board() + "\nSa vue:\n " + game.player_two.print_view())

def setup(client):
    client.add_cog(Battle(client))