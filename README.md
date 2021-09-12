# discord.py-tutorial-
discord.py Bot Tutorial


# WARNING
To protect your bot token (if you're using public editors) create a `.env` file and the code should be TOKEN=bot_token replace bot_token with your bot token and after doing that change bot token area to "client.run(os.getenv(TOKEN))".


----------------------------------------------------------------------------------------------------------------------------------------

# bot.py Example:

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") #You can replace ! with your bot prefix.

@bot.event #Ready event
async def on_ready():
  print("Ready!")
  
@bot.command() #sample command
async def echo(ctx):
  await ctx.send("Hello World")
  
@bot.event #Bot activity ready event.
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hello World"))

bot.run("Bot Token") #Read README.md
