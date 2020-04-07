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
        for game in self.game_list:
            if p_id == game.player_one.id or p_id == game.player_two.id:
                return True
            else:
                return False


    @commands.command(pass_context = True , name = "start_battle", description = "Lance une bataille")
    async def start_battle(self, ctx, opponent : discord.Member):
        await ctx.message.channel.purge(limit = 1)
        await ctx.message.channel.send(f"{ctx.message.author.mention} lance un défi à {opponent.mention}")
        channel = await opponent.create_dm()
        print(ctx.message.author.name, opponent.name, ctx.message.author.id, opponent.id)
        player_one_name = ctx.message.author.name
        player_one_id = ctx.message.author.id
        player_two_name = opponent.name
        player_two_id = opponent.id
        game = battle.create_game(player_one_name, player_two_name, player_one_id, player_two_id)
        self.game_list.append(game)
        channel = await ctx.message.author.create_dm()
        content = f"Place tes bateaux\n{game.player_one.print_view()}"
        await channel.send(content)
        channel = await opponent.create_dm()
        content = f"Place tes bateaux\n{game.player_two.print_view()}"
        await channel.send(content)

    @commands.command(pass_context = True, name =  "place", description =  "Permet de placer ses bateau")
    async def place_boats(self, ctx, *boats):
        if ctx.message.guild == None:
            if self.in_game(ctx.message.author.id):
                print("ok")
            else:
                print("pas ok")


    @commands.command(pass_context = True, name =  "fire", description =  "Tire")
    async def fire(self, ctx, case_name):
        if ctx.message.guild == None:
            if in_game(ctx.message.author.id):
                #rajouter une fonction de recherche de la game après avoir checké son existence
                game = in_game(ctx.message.author.id) 
                channel = await ctx.message.author.create_dm()
                if ctx.message.author.id == game.player_one.id:
                    target_statut = game.player_two.board.index(case_name).get_statut
                    if target_statut == 3:
                        await channel.send("Vous avez déjà touché sur cette case")
                    elif target_statut == 2:
                         await channel.send("Vous avez déjà tiré ici, sans succès")
                    elif target_statut == 1:
                        game.player_two.board.index(case_name).change_statut(3)
                        game.player_one.view.index(case_name).change_statut(3)
                        await channel.send("Touché !!")
                    elif target_statut == 0:
                        game.player_two.board.index(case_name).change_statut(2)
                        game.player_one.view.index(case_name).change_statut(2)
                        await channel.send("Plouf")



                    
def setup(client):
    client.add_cog(Battle(client))