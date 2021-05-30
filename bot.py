import random
import math
import time
import os
import discord
import youtube_dl

# import youtube_dl

# from random import choice
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='.')

#detail about member of chat
listOfMember = {
    "Tashee":702740671186075659,
    "BOSS BABY":488061960974237696,
    #bot owner
    "ThousandFaces":578333246618599458,
    "Kanita":812189623315857430,
    #admin
    "Iambo":567788833266204672
}

levelOnePower = ["PrincipleAdept", "Iambo"]

#check commands
def checkPermissionLevelOne(ctx):
    return ctx.author.name == levelOnePower[0] or ctx.author.name == levelOnePower[1]

#Event section
@client.event
async def on_ready(): 
    print("Bot ready")
    #activity = discord.Game(''Game name') to vhange into playing game
    #status = discord.status.(a type of status) for changing bot status
    #overall code should look like:     await client.change_presence(status = discord.status.(a type of status), discord.Game(''Fornite'))
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'Hentai Haven'))

@client.event
async def is_playing():
    print(f'{discord.client.User.display_name}')

@client.event
async def on_member_join(member):
    print(f'{member} has join a server')
    
@client.event 
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.event
async def on_connect():
    print(f'someone has connected to the server')

@client.event
async def on_disconnect():
    print('someone has disconnected')

# Events for errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(f'{ctx.author.name} is not worthy enough to weild such power.')
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(f'Dear {ctx.author.name}, the command used does not exist. Please contact tech support for more detail or if you want to add the said command as a new command.')
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name} is bad at typing. {ctx.author.name} can not even type in a bot command properly')
    else:
        return

#Command section
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency*1000)}ms')

@client.command()
async def server(ctx):
	guild = ctx.guild
	await ctx.send(f'Server Name: {guild.name}')
	await ctx.send(f'Server Size: {len(guild.members)}')
	await ctx.send(f'Server Name: {guild.owner}')

@client.command(name='load', help = 'Load a cog, not a Cock.')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(name='unload', help = 'Unload a cog, not a Cock.')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command(name='reload', help = 'Reload a cog if there are changes made in cog while server is up.')
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# For cog loading and changing from py files into cog files 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODE2NTg1OTY3NDMxMTg4NTEw.YD9G8g.XJDFdWASvY2n38Bf_XqO7N4Sdk8')
