import discord
from discord.ext import commands
import functions.load_config as c

bot = c.BotConfig()
client = commands.Bot(command_prefix= bot.prefix)

client.remove_command("help") #retire la commande help
extensions = ['commands.tools', 'commands.configuration_servers'] #listes des extensions à charger
if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f"{extension} a bien était chargée")
        except Exception as error:
            print(f"{extension} ne peut pas être chargée, {error}")

@client.event
async def on_ready(): 
    print('Bot is ready')
    await client.change_presence(status=discord.Status.online, activity= discord.Game("e/help"))

@client.event
async def on_member_join(member):
    print(f'{member} à rejoint le serveur')

@client.event
async def on_member_remove(member):
    print(f'{member} à quitté le serveur')

client.run(bot.bot_token())