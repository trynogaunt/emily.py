import discord
from index import client

def delete_emoji():
    all_emojis = client.emojis
    for emoji in all_emojis:
        