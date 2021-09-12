import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def echo(ctx):
    await ctx.send('Hello World')

bot.run('TOKEN')
