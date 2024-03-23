import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
  print("we logged in bois")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  await message.channel.send(",,,,,,")

client.run(TOKEN)
