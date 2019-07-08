import mysql.connector
import discord
from discord.ext import commands, tasks
import time
import emoji
import functions.load_config as c

def connection():
    return mysql.connector.connect(host= c.database_host, user= c.database_user, passwd= c.database_mdp, database= c.database_name)

def existing_server(ctx, password):
    identif = ctx.guild.id
    database = connection()
    existing_cursor = database.cursor()
    req = "SELECT * FROM serveurs WHERE Serverpassword = %s AND ServerId = %s"
    passw = (str(password), int(identif))

    existing_cursor.execute(req, passw)

    end = existing_cursor.fetchall()
    database.close()
    return end


def setup_channels(ctx, cursor, database):
    identif = ctx.guild.id
    guilds_channels = ctx.guild.channels
    reqChannel = "INSERT INTO channels(ChannelId, ChannelName, ChannelType, ChannelServer) VALUES(%s, %s, %s, %s)"

    val_channel = []
    for channel in guilds_channels:
        channel_id = channel.id
        channel_name = channel.name
        channel_name = channel_name
        channels_type = channel.type
        channel_type = f"{channels_type}"
        sql_tuple = (channel_id, channel_name,channel_type, identif)
        val_channel.append(sql_tuple)

    cursor.executemany(reqChannel, val_channel)
    database.commit()

def setup_server(ctx, password):
    identif = ctx.guild.id
    name = ctx.guild.name
    owner = ctx.guild.owner.name
    
    reqServ = "INSERT INTO serveurs(ServerId, ServerName, ServerOwner, ServerPassword) VALUES(%s, %s, %s, %s)"
   

    print (f"N° du serveur: {identif} \nNom du serveur: {name} \nSon possesseur: {owner} \nLe mot de passe: {password}")
    database = connection()
    data_cursor = database.cursor()
    val_server = [(identif, name, owner, password)]
    data_cursor.executemany(reqServ, val_server)
    database.commit()
    
    setup_channels(ctx, data_cursor, database)
    print ("Enregistrement des channels....")
    time.sleep(10)
    data_cursor.close()

    print ("Serveur enregistré")

def delete_server(ctx, password):

    end = existing_server(ctx, password)
    if len(end) < 1:
        return False
    else:
        database = connection()
        delete_cursor = database.cursor()
        identif = ctx.guild.id
        delete_id = (identif, )
        sql = "DELETE FROM serveurs WHERE ServerId = %s "
        delete_cursor.execute(sql, delete_id)
        database.commit()

        sql = "DELETE FROM channels WHERE ChannelServer = %s "
        
        delete_cursor.execute(sql, delete_id)
        database.commit()
        delete_cursor.close()
        database.close()
        return True

def rewrite_server(ctx, password):
    end = existing_server(ctx, password)
    if len(end) < 1:
        return False
    else:
        identif = ctx.guild.id
        database = connection()
        rewrite_cursor = database.cursor()   
        req = "SELECT ChannelName, ChannelType FROM channels WHERE ChannelServer = %s"
        server = (identif, )
        rewrite_cursor.execute(req, server)
        result = rewrite_cursor.fetchall()
        return result