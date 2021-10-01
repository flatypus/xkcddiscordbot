import discord
import requests
from bs4 import BeautifulSoup
import random

client = discord.Client()

def getxkcdquote():
    URL = f"https://xkcd.com/{random.randint(1,2000)}/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "lxml")
    breme = soup.find_all("a")
    png = ''
    for _ in breme:
        item = str(_)
        if "https://imgs.xkcd.com/" in item:
            png = item
    return((png.split('>')[1]).split('<')[0])

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!xkcd':
        xkcd = getxkcdquote()
        await message.channel.send(xkcd)        

client.run(TOKEN) #YOUR DISCORD TOKEN HERE
