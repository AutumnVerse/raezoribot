import discord
from discord.ext import commands
import requests
from bs4 import *

bot = commands.Bot(command_prefix='!')

print("connected!")
@bot.event
async def on_message(message):
    if message.content.startswith('!upload'):
        if message.attachments:
            attachment = message.attachments[0]
            download_url = attachment.url
            print(download_url)

            link = "http://raezorigdps.7m.pl/database/tools/songAdd.php"
            data = {"songlink": download_url}
            response = requests.post(link, data=data)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                song_id = soup.find('b').text
                await message.channel.send(f"New Song ID: {song_id}")
            else:
                print("Failed!")


bot.run('MTA5MDgxNzYyNDg5MzU3MTA5Mw.GlR1zJ.6tPcfTjhtJc2ibIyaB9Lk7C5fR7WEDtNbCbb2M')
