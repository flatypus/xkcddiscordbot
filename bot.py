import discord
import requests
from bs4 import BeautifulSoup
import random

client = discord.Client()

def gettext(info):
    return(((info).split('>')[1]).split('<')[0])

def getxkcdquote():
    URL = f"https://xkcd.com/{random.randint(1,2000)}/"
    page = requests.get(URL)
    content = BeautifulSoup(page.content, "lxml")
    title = str(content.find(id='ctitle'))
    a = content.find_all("a")
    picturelink = ''
    for _ in a:
        item = str(_)
        if "https://imgs.xkcd.com/" in item:
            picturelink = item
    return([gettext(picturelink),gettext(title)])

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!xkcd':
        image = getxkcdquote()[0]
        title = getxkcdquote()[1]
        embed=discord.Embed(title=title)
        embed.set_image(url=image)
        await message.channel.send(embed=embed)      

client.run(YOUR TOKEN GOES HERE)
