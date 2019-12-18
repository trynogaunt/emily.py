import mysql.connector
import functions.load_config as c

bot = c.BotConfig()

def add_server(bot, p_server_id, p_server_name, p_owner_id, p_owner_name):
    database = mysql.connector.connect(host= bot.database["Host"], user= bot.database["User"], passwd= bot.database["Mdp"], database= bot.database["Name"])
    ping = database.cursor()
    query = (f"INSERT INTO servers (server_id, server_name, owner_id, owner_name) VALUES (%s, %s, %s, %s)")

    ping.execute(query, (p_server_id, p_server_name, p_owner_id, p_owner_name))
    ping.close()
    database.close()

def add_channels(bot, p_server_id, p_channel_name, p_channel_cat):
    database = mysql.connector.connect(host= bot.database["Host"], user= bot.database["User"], passwd= bot.database["Mdp"], database= bot.database["Name"])
    ping = database.cursor()
    query = (f"INSERT INTO channels (server_channel_id, channel_name, channel_type, channel_cat)")
    