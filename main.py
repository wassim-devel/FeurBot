import discord
from random import randint

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Liste des différentes possibilités de message ainsi que leurs réponses
possibilites = {"quoi": ["feur", "chi", "driceps"], "oui": ["stiti", "ghours"], "mere": ["méditérannée", "rie"], "mère": ["méditérannée", "rie"]}

def retirer_points(message):
    caracteres = "!? ."
    message = message.lower()
    for x in range(len(caracteres)):
        message = message.replace(caracteres[x],"")
    return message


@client.event
async def on_ready():
    print(f'Je me suis bien connecté en tant que {client.user}')

@client.event
async def on_message(message):
    #On vérifie que ce n'est pas nous même (le bot) qui envoie le message
    if message.author == client.user:
        return

    # Si le contenu du message dont on a enlevé la ponctuation et les espaces termine par un des mots listés dans le dictionnaire possibilites, alors répondre au hasard une des réponses présente dans la liste correspondante
    for i in possibilites:
        if retirer_points(message.content).endswith(i): 
            await message.channel.send(possibilites[i][randint(0, len(possibilites[i]) - 1)])


client.run('TOKEN')
