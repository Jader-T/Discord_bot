import discord
from discord.ext import commands

class manager(commands.Cog):
    """Gerenciador do bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def initial(self):
        print('Estou pronto')
def setup(bot):
    bot.add_cog(manager(bot))