import discord
from decouple import config
from discord.ext import commands

bot = commands.Bot("$")

bot.load_extension("commands.manager")
bot.load_extension("commands.talks")

TOKEN = config("TOKEN")
bot.run(TOKEN)