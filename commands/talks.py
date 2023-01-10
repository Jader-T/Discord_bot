from discord.ext import commands

class talks(commands.Cog):
    """CONVERSAS COM O USER"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi')
    async def hello(self, ctx):
        nome = ctx.author.name
        await ctx.send(f"Olá, {nome}!")

    @commands.command()
    async def commands(self, ctx):
        comandos = "**invocation symbol**: $\n" + "**Commands**: commands, oi"
        await ctx.send(comandos)
def setup(bot):
    bot.add_cog(talks(bot))

