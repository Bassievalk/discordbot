import discord
import youtube_dl
import logging
import aiohttp
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from itertools import cycle

extention = (
                'Music'
            )

bot = commands.Bot (command_prefix = ".")
bot.remove_command('help')
status = ['.help', 'Op de ThanatosClan']

async def change_status():
    await bot.wait_until_ready()
    berichten = cycle(status)

    while not bot.is_closed:
        current_status = next(berichten)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print ("Bot geladen!") 

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot



@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def kick(ctx, user: discord.Member):
    await bot.say("Toedeloee".format(user.name))
    await bot.kick(user)


bot.loop.create_task(change_status())

bot.run("")
