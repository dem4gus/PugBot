import json
import requests
import random
outPrime = "Test"
primeList = []
primeList = json.loads(open('data.json').read())

def det_prime(inp):
    num = inp
    tempNum = inp - 1
    while tempNum > 1:
        if num % tempNum == 0:
            return "No"
        if num % tempNum != 0:
            tempNum -= 1
        if tempNum == 2:
            return "Yes"
async def prime(client, message):
    try:
        i = str(message.content).split(' ')
        output = "Too Long"
        if len(i) == 1:
            randomPrime = random.choice(primeList)
            output = str(randomPrime) + " is a prime number."
        if len(i) == 2:
            if int(i[1]) < 100000:
                output = det_prime(int(i[1]))
        await client.send_message(message.channel, output)
            
    except Exception as e:
        print(e)
        await client.send_message(message.channel, "ERROR. Not a valid number")
