


def make_message():
    return ('```***    ***  ***   ***  ***   ***  ***   ***\n'
            '***    ***  ***   ***  ***   ***  ***   ***\n'
            '***    ***  ***   ***  ***   ***  ***   ***\n'
            '**********  *********  *********  *********\n'
            '**********  *********  *********  *********\n'
            '       ***        ***        ***        ***\n'
            '       ***        ***        ***        ***\n'
            '       ***        ***        ***        ***\n```')



async def four(client, message):
    output = make_message()*4
    await client.send_message(message.channel, output)
