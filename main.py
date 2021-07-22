import discord

from discord.ext import commands

import random

client = commands.Bot(command_prefix = "!", case_insensitive = True)

@client.event

async def on_ready():

  print('Entramos como {0.user}' .format(client))

@client.command()

async def ola(ctx):

  await ctx.send(f'Olá, {ctx.author}')

@client.command()

async def rolar(ctx, numero):

  variavel = random.randint(1,int(numero))

  await ctx.send(f'> *A rolagem foi feita.. caiu no número* **{variavel}**')

@client.command()

async def abespadanorte(ctx):

  embed = discord.Embed(

    title = '*Ataque básico: Estilo de espada do norte*',

    description = 'tests',

    colour = 11598249

  )

  embed.set_thumbnail(url='')

  embed.set_image(url='')

  await ctx.send(embed = embed)

client.run('ODY3NDIzNjgzNjc3MjU3NzM4.YPg5Qg.TZC45Po66cRnYWq5fdLFcL5dffc')
