import discord
import os
from stayalivefile import stayalive

client = discord.Client()


@client.event
async def on_ready():
    print('sto funzando'.format(client))
    stayalive()


@client.event
async def on_message(message):
    if message.content.startswith('?midissocio'):
        await message.channel.send('mi dissocio da tutto')
        await message.channel.send(
            'https://media.giphy.com/media/wsZ9rcSX4vsNHnZKbj/giphy.gif')
        await message.channel.send(':white_check_mark: 100% dissociato')

    if message.content.startswith('?miassocio'):
        await message.channel.send('ok bro')
        await message.channel.send(
            'https://media.giphy.com/media/804TNmnYLfNao/giphy.gif')
        await message.channel.send(':white_check_mark: 100% Associato')

    if message.content.startswith('?bestconsole'):
        await message.channel.send('ovviamente xbox')
        await message.channel.send(
            'https://media.giphy.com/media/436nEx1eDthJluQ4mJ/giphy-downsized-large.gif'
        )
        await message.channel.send(':white_check_mark: scelta giusta fatta =)')

    if message.content.startswith('?help'):
        await message.channel.send(
            'commands here:https://replit.com/@star08-web/midissocibotservice#commands.md '
        )

    if message.content.startswith('?about'):
        await message.channel.send('Dissociatore Professionista')
        await message.channel.send(
            'original idea by: https://github.com/parliamodipc/dissociatoreprofessionista'
        )
        await message.channel.send('written by star08-web')
        await message.channel.send(
            'running on Alexandra Moderation Service (replit env) ')
        await message.channel.send('©️ 2022 star08-web')


client.run(os.environ['token'])
