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
    
    def in_game(self, p_id):
        for game in game_list:
            if p_id == game.player_one.id or p_id == game.player_two.id:
                return game_list.index(game)

    @commands.command(pass_context = True , name = "start_battle", description = "Lance une bataille")
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

    @commands.command(pass_context = True, name =  "fire", description =  "Tire")
    async def fire(self, ctx, case_name):
        if ctx.message.channel.is_private and in_game(ctx.message.author.id):
            game_index = in_game(ctx.message.author.id)

def setup(client):
    client.add_cog(Battle(client))