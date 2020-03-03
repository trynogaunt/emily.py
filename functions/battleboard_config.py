import random
import discord

class Case():
    def __init__(self, p_pos:str):
        self.pos = p_pos
        self.statut = 0
    
    def change_statut(self, p_statut:int):
        self.statut = p_statut

class Game():
    def __init__(self, p_player_one, p_player_two):
        self.player_one = p_player_one
        self.player_two = p_player_two


class Player():
    def __init__(self, p_name,p_discord_id, p_board:list):
        self.name = p_name
        self.id = p_discord_id
        self.score = 0
        self.board = p_board
        self.view = p_board
    
    def print_board(self):
        ligne = 1
        message = ""
        for pos_case in self.board:
            if ligne > 11:
                message = message + "\n"
                ligne = 1
            elif pos_case.statut == 0:
                message = message + "0 | "
                ligne = ligne + 1
            elif pos_case.statut == 1:
                message = message + "X | "
                ligne = ligne + 1
            else:
                message = message + "B | "
                ligne = ligne + 1
        return message
    
    def print_view(self):
        ligne = 1
        message = ""
        for pos_case in self.board:
            if ligne > 11:
                message = message + "\n"
                ligne = 1
            elif pos_case.statut == 0:
                message = message + "0 | "
                ligne = ligne + 1
            elif pos_case.statut == 1:
                message = message + "X | "
                ligne = ligne + 1
            else:
                message = message + "B | "
                ligne = ligne + 1
        return message



def create_game(p_player_one:discord.User, p_player_two:discord.User): 
    cases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    list_Case = []
    for pos in cases:
        for i in range(0,12):
            case = Case(f"{pos}{i}")
            list_Case.append(case)
    player_1 = Player(p_player_one.name, p_player_one.id, list_Case)
    player_2 = Player(p_player_two.name, p_player_two.id, list_Case)
    game = Game(player_1, player_2)
    return game



