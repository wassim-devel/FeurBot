import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dictionnaire = {"quoi": ["feur", "chi", "driceps"], "oui": ["stiti", "ghours"]}

@client.event
async def on_ready():
    print(f'Oeoe je me suis bien log en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    await message.channel.send((dictionnaire[message.content.lower()])[random.randint(0, len(dictionnaire[message.content.lower()])-1)])
    

client.run('TOKEN')