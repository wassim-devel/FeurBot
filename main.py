import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dictionnaire = {"quoi": ["feur", "chi", "driceps"], "oui": ["stiti", "ghours"]}

def retirer_points(y):
    caracteres = "!? ."
    y = y.lower()
    for x in range(len(caracteres)):
        y = y.replace(caracteres[x],"")
    return y


@client.event
async def on_ready():
    print(f'Oeoe je me suis bien log en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    for i in dictionnaire.keys():
        if i == retirer_points(message.content)[-len(i):]:
            
            await message.channel.send(dictionnaire[retirer_points(message.content)[-len(i):]][random.randint(0,len(dictionnaire[retirer_points(message.content)[-len(i):]])-1)])
    
    

client.run('TOKEN')
