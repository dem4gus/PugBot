import requests
import json

config = json.loads(open('config.json').read())  # Load Configs
stamps = json.loads(open('timestamps.json').read())
API_KEY = config["blizzard_api_key"]

def get_name(item):
    l = requests.get("https://us.api.battle.net/wow/item/%s?locale=us&apikey=%s" % ( item, API_KEY))
def get_guild(guild, server):
    r = requests.get("https://us.api.battle.net/wow/guild/%s/%s?fields=news&locale=us&apikey=%s" % (
            server, guild, API_KEY))
    if r.status_code != 200:
        raise Exception("Could Not Find Character (No 200 from API)")
    guild_dict = json.loads(r.text)
    for event in  guild_dict["news"]:
        if "bonusLists" in event:
            if event["context"] = "":
                timestamp = event["timestamp"]
                character = event["character"]
                item = event["itemId"]
                itemName = get_name(item)



async def news(client, message):
    try:
        i = str(message.content).split(' ')
        guild = i[1]
        server = i[2]
        character_info = get_guild(guild, server)
        await client.send_message(message.channel, character_info)
