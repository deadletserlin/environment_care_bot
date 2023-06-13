
import discord
from discord.ext import commands
import random, os

intents = discord.intents.default()
intents.message_content = True

# kenalkan bot-nya
bot = commands.Bot(command_prefix='$', intents=intents)

# buat reaksi dn command untuk bot-nya

@bot.event # agar bot bereaksi ktika ad sesuatu
async def on_ready(): # ktika bot siap
    print('BOT TELAH SIAP!')

@BOT.COMMAND() # Untuk
async def kerajinan(ctx):
    img_name = random.choice(os.lisdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as gambar: # membuka file gambar dn disimpan di vriable
        picture = discord.File(gambar)
    await ctx.send(picture)

bot.run('yor token')
