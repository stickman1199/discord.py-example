import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("Ready!")
  
@client.command()
async def echo(ctx):
  await ctx.send("Hello World")
  
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hello World"))

client.run("Bot Token")
