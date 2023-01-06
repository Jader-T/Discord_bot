import discord
from discord.ext import commands

neto = commands.Bot("$")

@neto.event
async def on_ready():
    print('Estou pronto')

@neto.command()
async def salve(ctx):
    await ctx.send("surfzada")

neto.run('MTA2MDg5ODczOTc4NDUyMzg3OA.G0XR18.zPOJgd3mjGWMHDXCSQUjPThcKiqwmEbOcZDmvw')