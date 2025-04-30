#04/30/2025 - First discord bot project - very simple calculator
#Name = BitBot
#Author(discord name) = xepherongd_

import os
import discord
from discord.ext import commands

from math import atan

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

PI = 4 * atan(1.0)

@bot.command(name="help")
async def help(ctx):
    await ctx.send("Available commands: \n!add \n!sub \n!mul \n!div")

@bot.command()
async def add(ctx, a, b):
    await ctx.send(f"{a} + {b} = {a + b}")

@bot.command()
async def sub(ctx, c, d):
    await ctx.send(f"{c} - {d} = {c - d}")

@bot.command()
async def mul(ctx, a, b):
    await ctx.send(f"{a} * {b} = {a * b}")

@bot.command()
async def div(ctx, a, b):
    await ctx.send(f"{a} / {b} = {a / b}")

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

bot.run(DISCORD_TOKEN)