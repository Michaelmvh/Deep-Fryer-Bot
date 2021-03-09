import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from deepfry import deepFryImage
from io import BytesIO

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='deepfry', pass_context=True)
async def deepfrycommand(context, arg):
    print(arg)
    #Converts our image object to Bytes to discord file
    with BytesIO() as image_binary:
        deepFryImage(arg).save(image_binary, 'PNG')
        image_binary.seek(0)
        await context.send(file=discord.File(fp=image_binary, filename='deepfried.png'))

        ## if deepfry for message

        ## if deepfry for quote 
        
        ## else deepfry previous image

client.run(TOKEN)