import random
def get_roll(inp):
    top = int(inp)
    randomNum = random.randint(1, top)
    return int(randomNum)
def get_message(in_num):
    top = int(in_num)
    result = get_roll(top)
    return_string = ''
    return_string += 'Rolling 1 - %s \n' % top
    return_string += 'Result: %s' % result

    return return_string
    
async def gamble(client, message):
    try:
        i = str(message.content).split(' ')
        num = i[1]
        await client.send_message(message.channel, get_message(num))
    except Exception as e:
        print(e)
        await client.send_message(message.channel, "ERROR. Not a valid number")
