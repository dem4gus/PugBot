import json
import requests
import discord
import pprint

def createCommand(client, message, server, commandName, newCommand):
    print("Creating Command")
    with open("customcommands.json") as cmds:
        customCommandsDict = json.load(cmds)
    print("File Opened")
    print(customCommandsDict)
    #customCommandsDict = fixLazyJson(customCommandsDict)
    #customCommandsDict = json.loads(open('customcommands.json').read())
    if str(server) not in customCommandsDict:
        customCommandsDict[server] = {}
    customCommandsDict[server][commandName] = newCommand
    for d in customCommandsDict[server]:
        print(d)
    pp_json(customCommandsDict)

    
def pp_json(json_thing, sort=True, indents=4):
    with open('customcommands.json', 'w') as outfile:
        if type(json_thing) is str:
            json.dump(json.loads(json_thing), outfile, sort_keys=sort, indent=indents)
        else:
            json.dump(json_thing, outfile, sort_keys=sort, indent=indents)

def det_admin(client, message):
    author = str(message.author)
    server = message.server
    serverID = message.server.id
    if message.author == server.owner or str(message.author) == "Bsep#0415":
        return True
    else:
        return False


async def create(client, message):
    author = str(message.author)
    server = message.server
    serverID = message.server.id
    try:
        i = str(message.content).split(' ')
        try:
            if i[1].startswith('!'):
                d = str(message.content).split(i[1])
                if det_admin(client, message) == True:
                    createCommand(client, message, str(serverID), i[1], d[1])
                else:
                    await client.send_message(message.channel, "Not valid user")
        except Exception as e:
            print(e)
            await client.send_message(message.channel, "Command Doesn't start with <!>")
    except Exception as e:
        print(e)
        await client.send_message(message.channel, "Error: No command input")

async def sendMessage(client, message):
    with open('customcommands.json') as df:
        customCommands = json.load(df)
    try:
        i = str(message.content).split(' ')
        server = str(message.server.id)
        command = i[0]
        msgSend = str(customCommands[server][command])
        print(msgSend)
        await client.send_message(message.channel, msgSend)
    except Exception as e:
        print(e)

def removeCmd(client, message, cmd):
    serverId = str(message.server.id)
    with open("customcommands.json") as cmds:
        customCommandsDict = json.load(cmds)
    if str(cmd) in customCommandsDict[serverId]:
        del customCommandsDict[serverId][cmd]
    pp_json(customCommandsDict)
            

    
async def deleteC(client, message):
    if det_admin(client, message) == True:
        try:
            i = str(message.content).split(' ')
            removeCmd(client, message, i[1])
        except Exception as e:
            print(e)
    else:
        await client.send_message(message.channel, "Invalid User")

async def commandHelp(client, message):
    server = str(message.server.id)
    return_string = "All Commands for your Server"
    return_string += "```"
    with open("customcommands.json") as cmds:
        customCommandsDict = json.load(cmds)
    for cmd in customCommandsDict[server]:
        print(cmd)
        return_string += "%s\n" % cmd
    return_string += "```"
    return_string += "Remove with !delete <!command>"
    
    await client.send_message(message.channel, return_string)
