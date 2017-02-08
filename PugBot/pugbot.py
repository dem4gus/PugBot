import discord
import json
import time
import itertools

# Commands #
from commands.pug import pug
from commands.prime import prime
from commands.gamble import gamble
from commands.guild import guild
from commands.four import *
from commands.create import create
from commands.create import sendMessage
from commands.create import deleteC
from commands.create import commandHelp

config = json.loads(open('config.json').read())  # Load Configs
DISCORD_TOKEN = config["discord_token"]
client = discord.Client()
testOfWillList = ["Bsep#0415"]
testOfWillList2 = ["Bsep#0415"]

crntMessages = ['!info', '!kill', '!pug', '!name', '!testofwill', '!hewillnotdivideus', '!man', '!guild', '!name', '!prime', '!roll', '!create', '!deleteC', '!commands']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    author = str(message.author)                   
    if message.content.startswith('!info') or message.content.startswith('!help'):
        await client.send_message(message.channel, "I'm BotSep, the pug analyzer!\n"
                                                   "Use: !pug <name> <server> <region> \n"
                                                   "Other commands: !roll <number>")
    if message.content.startswith('!kill'):
        await client.send_message(message.channel, "That's rude")

    if message.content.startswith('!pug'):
        await pug(client, message)

    if message.content.startswith('!create'):
        await create(client, message)

    if message.content.startswith('!'):
        msgD = (message.content).split(' ')
        if msgD[0] not in crntMessages:
            await sendMessage(client, message)
        
    if message.content.startswith('!name'):
        if author == 'Bsep#0415':
            try:
                i = str(message.content).split(" ")
                await client.edit_profile(username=i[1])
            except Exception as e:
                print(e)
                
    if message.content.startswith('!delete'):
        await deleteC(client, message)

    if message.content.startswith('!commands'):
        await commandHelp(client, message)
        
    if message.content.startswith('!testofwill'):
        if author in testOfWillList:            
            if author in testOfWillList2:
                await client.send_message(message.channel, "You have will")
            else:
                await client.send_message(message.channel, "You have no will")
                testOfWillList2.append(author)
        else:
            await client.send_message(message.channel, "You have no will")
            testOfWillList.append(author)
    if message.content.startswith('!hewillnotdivideus'):
        await client.send_message(message.channel, "REEEEEEEEEEEEEeeEEEeeeEEEeeEeEe")

    if message.content.startswith('4'):
        if author == 'pudding794[Ret]#8502' or author == 'Bsep#0415' or author == 'C0nsp1racy#8055':
            await four(client, message)
        
    #if str(message.author) == 'pudding794[Ret]#8502':
        #await client.send_message(author, "FUCK OFF M8")
        
    if message.content.startswith('!man'):
        await client.send_message(message.channel, "MAAAAN https://www.youtube.com/watch?v=6E5m_XtCX3c")
        
    if message.content.startswith('!guild'):
        if author == 'Bsep#0415' or author == 'Rudamen#9234':
            await guild(client, message)
        else:
            await client.send_message(message.channel, "Invalid User")

    if message.content.startswith('!prime'):
        await prime(client, message)

    if message.content.startswith('!roll'):
        await gamble(client, message)
        
client.run(DISCORD_TOKEN)
