import discord
from key import token
import pandas as pd
import subprocess

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
        def ler_arquivo_xls(nome_arquivo):
        # Lê o arquivo XLS
        df = pd.read_excel(nome_arquivo)

        # Converte o conteúdo em texto
        texto = df.to_string(index=False)

        return texto

    # Nome do arquivo XLS a ser lido
    nome_arquivo = "exames.xlsx"

    # Chama a função para ler o arquivo e obter o texto
    texto_arquivo = ler_arquivo_xls(nome_arquivo)
    
    if message.content.startswith('/exames'):
        ler_arquivo_xls(nome_arquivo)
        await message.channel.send(texto_arquivo)

    if message.content.startswith('/configesmeralda'):
        await message.channel.send('Aguarde a configuração')
        executar_script_vbs(caminho_script)


client.run(TOKEN)
