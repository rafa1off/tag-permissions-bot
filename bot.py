import os
import discord
from quotes import Quotes as quote
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='add', help=quote.add_command)
@commands.has_permissions(administrator=True)
async def add(ctx, *users: discord.Member):
    if users:
        for user in users:
            channel = bot.get_channel(ctx.channel.id)
            await channel.set_permissions(user, view_channel=True, send_messages=True, add_reactions=True)
    else:
        await ctx.send(quote.specify_user)


@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(quote.missing_permissions)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(quote.member_not_found)


@bot.command(name='remove', help=quote.remove_command)
@commands.has_permissions(administrator=True)
async def remove(ctx, *users: discord.Member):
    if users:
        for user in users:
            channel = bot.get_channel(ctx.channel.id)
            await channel.set_permissions(user, overwrite=None)
    else:
        channel = bot.get_channel(ctx.channel.id)
        for member in channel.members:
            await channel.set_permissions(member, overwrite=None)


@remove.error
async def remove_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(quote.missing_permissions)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(quote.member_not_found)


@bot.command(name='members')
@commands.is_owner()
async def members(ctx, *users: discord.Member):
    pass


bot.run(token)
