import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

liste = ["quoi", "feur", "oui", "stiti", "non", "bril"]

@client.event
async def on_ready():
    print(f'Oeoe je me suis bien log en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for i in range(len(liste)):

        if message.content.lower().startswith(liste[i]) and i%2 == 0:
            await message.channel.send(liste[i+1])
    

client.run('MTA0MTMyMjMwNTU3MTI3MDY4Nw.G7-0fN.IQ0tJUMPMExMmZsxVOKDQvVX6BplVYB_Ii6z48')