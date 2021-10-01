import discord
import requests
from bs4 import BeautifulSoup
import random

client = discord.Client()

def getxkcdquote():
    URL = f"https://xkcd.com/{random.randint(1,2000)}/"
    page = requests.get(URL)
    content = BeautifulSoup(page.content, "lxml")
    a = content.find_all("a")
    picturelink = ''
    for _ in a:
        item = str(_)
        if "https://imgs.xkcd.com/" in item:
            picturelink = item
    return(((picturelink).split('>')[1]).split('<')[0])

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

client.run(YOUR_TOKEN_HERE)
