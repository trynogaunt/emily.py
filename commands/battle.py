import discord
import asyncio
from discord.ext import commands
import functions.battleboard_config as battle
import functions.load_config as c

class Battle(commands.Cog, name="battle"):
    def __init__(self, client):
        self.client = client
        self.bot = c.BotConfig()
        self.game_list = []

    @commands.command(pass_context = True , name = "start_battle", description = "test")
    async def start_battle(self, ctx, opponent : discord.Member):
        await ctx.message.channel.purge(limit = 1)
        await ctx.message.channel.send(f"{ctx.message.author.mention} lance un défi à {opponent.mention}")
        channel = await opponent.create_dm()
        game = battle.create_game(ctx.message.author, opponent)
        self.game_list.append(game)
        channel = await ctx.message.author.create_dm()
        content = f"Place tes bateaux\n{game.player_one.print_view()}"
        await channel.send(content)
        channel = await opponent.create_dm()
        content = f"Place tes bateaux\n{game.player_two.print_view()}"
        await channel.send(content)

def setup(client):
    client.add_cog(Battle(client))