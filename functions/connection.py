import mysql.connector
import functions.load_config as c

bot = c.BotConfig()

def database_connection(bot):
    return mysql.connector.connect(host= bot.database_host, user= bot.database_user, passwd= bot.database_mdp, database= bot.database_name)

def database_disconnect(pconnection):
    pconnection.disconnect()
    