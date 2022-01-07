import discord
import os
from discord import client
from discord.ext import commands
import dotenv
from config import TOKEN


dotenv.load_dotenv(dotenv_path="./.env/config")#où se trouve le token

intents = discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True)
bot = commands.Bot(command_prefix="*",intents=intents)
bot.remove_command('help') # ajout du help perso

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="le serveur"))
    print("Le bot est bien connecté.")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['TOKEN'])
