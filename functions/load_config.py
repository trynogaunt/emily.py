import json
import discord
from discord.ext import commands


class BotConfig():
    name, __token, prefix, no_help, database = None, None, None, None, None

    def __init__(self):
        self.construct_config()

    def bot_token(self):
        return self.__token

    def construct_config(self):
        with open('functions/config.json', 'r') as data_config: #récupère les informations de configuration du bot dans "functions/config.json"
            p_data_config = json.load(data_config)
            self.name = p_data_config["Name"]
            self.__token = p_data_config["Token"]
            self.prefix = p_data_config["Prefix"]
            self.no_help = p_data_config["No_help_command"]
            self.database = p_data_config["Database"]
            self.client = commands.Bot(command_prefix=self.prefix)