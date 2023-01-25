import discord
from decouple import config
from discord.ext import commands
import math
bot = commands.Bot("$")

bot.load_extension("commands.manager")
bot.load_extension("commands.talks")
bot.load_extension("commands.calc")
TOKEN = config("TOKEN")
bot.run(TOKEN)
