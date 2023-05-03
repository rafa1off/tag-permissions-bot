import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name='add')
async def add(ctx, *users: discord.Member):
    if discord.utils.get(ctx.guild.roles, name='Gazebos') in ctx.author.roles:
        for user in users:
            await ctx.send(user.roles)
    else:
        await ctx.send('Not enough permissions')

bot.run(token)
