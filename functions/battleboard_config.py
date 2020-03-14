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
        end_line = 0
        line_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        line_number = 0
        statut_print = [0 , "X", "B"]
        message = f"```\n\ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9\n{line_letter[line_number]} "
        line_number += 1
        for i in self.view:
            if end_line < 9:
                message += f"{statut_print[i.statut]} | "
                end_line = end_line + 1
            else:
                if line_number == 10:
                    message += f"{statut_print[i.statut]}"
                    pass
                else:
                    message += f"{statut_print[i.statut]}\n{line_letter[line_number]} "
                    end_line = 0
                    line_number += 1
                
        message += "```"
        return message
    
    def print_view(self):
        end_line = 0
        line_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        line_number = 0
        statut_print = [0 , "X", "B"]
        message = f"```\n\ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9\n{line_letter[line_number]} "
        line_number += 1
        for i in self.view:
            if end_line < 9:
                message += f"{statut_print[i.statut]} | "
                end_line = end_line + 1
            else:
                if line_number == 10:
                    message += f"{statut_print[i.statut]}"
                    pass
                else:
                    message += f"{statut_print[i.statut]}\n{line_letter[line_number]} "
                    end_line = 0
                    line_number += 1
                
        message += "```"
        return message



def create_game(p_player_one:discord.User, p_player_two:discord.User): 
    cases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    list_Case = []
    for pos in cases:
        for i in range(0,10):
            case = Case(f"{pos}{i}")
            list_Case.append(case)
    player_1 = Player(p_player_one.name, p_player_one.id, list_Case)
    player_2 = Player(p_player_two.name, p_player_two.id, list_Case)
    game = Game(player_1, player_2)
    return game



