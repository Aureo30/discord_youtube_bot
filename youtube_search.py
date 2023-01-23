# import des modules qui servent au bon fonctionement du programme
from youtubepy import Video
import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("Ready !")

@bot.commande()
async def youtube(ctx, title):
    video = Video(title)
    result = video.search()
    await ctx.send(result)