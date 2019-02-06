# Work with Python 3.6
import discord
import configparser
import random
from asyncio import sleep

config = configparser.ConfigParser()
config.read('secrets.ini')
TOKEN = config['AUTH']['TOKEN']

client = discord.Client()



#stolen from rce
def head_or(xs, default=None):
    return next(iter(xs), default)

def parse_cmd(input, prefix="!"):
    if not input.startswith(prefix):
        return None, None
    cmd, *arg = input.strip(prefix).split(' ', 1)
    return cmd.lower(), head_or(arg, "")


async def get_cmd(msg):
    return msg.replace('!')

@client.event
async def on_message(message):

    content = message.content

    if message.author.bot:
        return

    cmd, arg = parse_cmd(content)
    if not cmd:
        return

    handler = commands.get(cmd)
    if not handler:
        return

    if handler:
        await handler(client, message, arg)
        return


async def cmd_coin(client, message, arg):
    await client.send_message(message.channel, "Flipping coin..")
    await sleep(1)
    await client.send_message(message.channel, "The coin lands on: %s" % random.choice(['Jaakko', 'Tuomas', 'Joonas', 'Vuan', 'Tommi']))

commands = {
    'coin' : cmd_coin
}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
