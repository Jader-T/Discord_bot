import discord
from discord.ext import commands

class manager(commands.Cog):
    lista_palavroes = []

    """Gerenciador do bot"""
    def __init__(self, bot):
        self.bot = bot
        ''''Leitura do arquivo e tratamento de palavrões'''
        arq = 'palavroes.txt'
        with open(arq) as fp:
            line = fp.readline()
            while line:
                manager.lista_palavroes.append(line.strip())
                '''print("{}".format(line.strip()))'''
                line = fp.readline()
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        #Tratamento de palavrões
        mensagem_user = message.content.lower().split()
        for x in mensagem_user:
            if x in manager.lista_palavroes:
                await message.channel.send(f'{message.author.name}, para de falar palavrão ai, ixtepô')
                await message.delete()
    @commands.Cog.listener()
    async def initial(self):
        print('Estou pronto')

def setup(bot):
    bot.add_cog(manager(bot))