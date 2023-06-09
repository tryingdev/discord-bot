import discord
from key import token, passwords, diretorio_publico
import pandas as pd
import subprocess

sasfal = passwords
pasta = diretorio_publico

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} está online!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/examespardini'):
        ler_arquivo_xls(nome_arquivo)
        await message.channel.send(texto_arquivo)

    if message.content.startswith('/configesmeralda'):
        await message.channel.send('Aguarde a configuração')
        executar_script_vbs(caminho_script)


client.run(TOKEN)
