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

def add_channels(bot,p_server_id, p_channel_name,p_channel_type, p_channel_cat):
    database = mysql.connector.connect(host= bot.database["Host"], user= bot.database["User"], passwd= bot.database["Mdp"], database= bot.database["Name"])
    ping = database.cursor()
    query = (f"INSERT INTO channels (server_channel_id, channel_name, channel_type, channel_cat) VALUES (%s, %s, %s, %s)")
    ping.execute(query, (p_server_id, p_channel_name, p_channel_type, p_channel_cat))
    ping.close()
    database.close()

def add_roles(bot, p_role_name, p_role_colour, p_role_hoist, p_role_mentionnable, p_role_id, p_role_position):
    database = mysql.connector.connect(host= bot.database["Host"], user= bot.database["User"], passwd= bot.database["Mdp"], database= bot.database["Name"])
    ping = database.cursor()
    query = (f"INSERT INTO roles (role_name, role_colour, role_hoist, role_mentionnable, role_id, role_position) VALUES (%s, %s, %s, %s, %s, %s)")
    ping.execute(query, (p_role_name, p_role_colour, p_role_hoist, p_role_mentionnable, p_role_roloid, p_role_position))
    ping.close()
    database.close()