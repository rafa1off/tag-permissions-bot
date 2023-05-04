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
@commands.has_permissions(administrator=True)
async def add(ctx, *users: discord.Member):
    for user in users:
        channel = bot.get_channel(ctx.channel.id)
        await channel.set_permissions(user, view_channel=True, send_messages=True, add_reactions=True)

@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Not enough permissions')

@bot.command(name='remove')
@commands.has_permissions(administrator=True)
async def remove(ctx, *users: discord.Member):
    for user in users:
        channel = bot.get_channel(ctx.channel.id)
        await channel.set_permissions(user, overwrite=None)

@remove.error
async def remove_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Not enough permissions')

bot.run(token)
