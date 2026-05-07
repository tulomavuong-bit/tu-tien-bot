import os
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="Q", intents=intents)

@bot.event
async def on_ready():
    print(f"Đăng nhập thành công: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🐧 Pong!")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
