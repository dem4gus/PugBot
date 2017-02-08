import requests
import json
from commands.pug import *

guild_raiders = requests.get("https://us.api.battle.net/wow/guild/Sargeras/Doppelganger?fields=members&locale=en_US&apikey=6dn7gkvnerfpsvfs373cejbya3hk2kmu")
guild_dict = json.loads(guild_raiders.text)
raiders = []
members = guild_dict["members"]
def get_total_raiders():
    for char in members:
        if char["rank"] == 7 or char["rank"] == 0 or char["rank"] == 1 or char["rank"] == 3:
            raiders.append(char["character"]["name"])
    return raiders
"""for char in members:
    if char["rank"] == 0:
        print("Guild Master: %") 
    if char["rank"] == 1:
        print(char["character"]["name"])
    if char["rank"] == 3:
        print(char["character"]["name"])
        raiders += 1"""

get_total_raiders()

async def guild(client, message):
    for s in raiders:
        name = s
        server = 'Sargeras'
        target_region = 'us'
        char_info = get_char(name, server, target_region)
        await client.send_message(message.channel, char_info)
