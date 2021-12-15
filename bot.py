# -*- coding: utf8 -*-

from discord_database import locals
from asyncio.tasks import sleep
from discord.ext import commands
from config import settings
from discord_webhook import DiscordWebhook, DiscordEmbed
import math
import discord
import random, string
from random import randrange
import asyncio

#переменные

bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')
px = settings['prefix']
cl = '0x440d54'

#@bot.event

@bot.event
async def on_ready():
    print('Bot launched successfully :)')
    print(f'My name is {bot.user.name}')
    print(f'My client id is {bot.user.id}')

#@bot.command


@bot.command()
async def nitro(ctx, num:int):
    value = 1
    while value <= num:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(code)
        value += 1

@bot.command()
async def лавписьмо(ctx):
    def check(msg):
        return msg.author == ctx.author and \
               msg.channel == ctx.channel
    await ctx.send("Заполни след. данные\nУкажи пользователя или его ID кому хочешь отправить любовное письмо.")
    msg1 = await bot.wait_for("message", check=check)
    await ctx.send("Укажи содержание письма.")
    msg2 = await bot.wait_for("message", check=check)
    trade1 = str(msg1.content)
    trade2 = str(msg2.content)

#error




                    
            
    
            








bot.run(settings['token'])