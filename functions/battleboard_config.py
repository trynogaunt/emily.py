import random

class Case():
    def __init__(self, p_pos:str):
        self.pos = p_pos
        self.statut = 0

class Board():
    def __init__(self, p_player_one:str, p_player_two:str, list_case:list):
        self.player_one = p_player_one
        self.player_two = p_player_two
        self.battleboard = list_case


def create_board():
    ligne = 1
    cases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    list_Case = []
    for pos in cases:
        for i in range(0,12):
            case = Case(f"{pos}{i}")
            list_Case.append(case)
    board = Board("Tryno", "Kheas", list_Case)
    message = ""
    for pos_case in board.battleboard:
        if ligne > 11:
            message = message + "\n"
            ligne = 1
        elif pos_case.statut == 0:
            message = message + "🔵 | "
            ligne = ligne + 1
        elif pos_case.statut == 1:
            message = message + "❌ | "
            ligne = ligne + 1
        else:
            message = message + "⛵ | "
            ligne = ligne + 1
    return message


