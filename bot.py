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

    def executar_script_vbs(caminho_script):
        try:
            subprocess.run(['cscript', caminho_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o script VBS: {e}")

    # Exemplo de uso
    caminho_script = configesmeralda.vbs

    def ler_arquivo_xls(nome_arquivo):
        # Lê o arquivo XLS
        df = pd.read_excel(nome_arquivo)

        # Converte o conteúdo em texto
        texto = df.to_string(index=False)

        return texto

    # Nome do arquivo XLS a ser lido
    nome_arquivo = "teste.xlsx"

    # Chama a função para ler o arquivo e obter o texto
    texto_arquivo = ler_arquivo_xls(nome_arquivo)

    # Imprime o texto
    print(texto_arquivo)

    if message.content.startswith('/nutri'):
        await message.channel.send(
            f'**Convênios que aceitam nutricionista** : '
            f'\n'
            f'\n ASFAL '
            f'\n ASSEFAZ '
            f'\n CASSI '
            f'\n FACHESF '
            f'\n FUNCEF '
            f'\n GEAP '
            f'\n LIFE '
            f'\n POSTAL '
            f'\n '
            f'\n '
            f'\n **O CONVÊNIO QUE NÃO ESTÁ NA LISTA NÃO ACEITA :D**')

    if message.content.startswith('/asfal'):
        await message.channel.send(
            f'**Autorizador Asfal** : '
            f'\n'
            f'\n **Link Autorizador**: https://asfal.dyndns-web.com/asfal/prestador/index.php '
            f'\n **Login**: 0156114783 '
            f'\n **Senha**: {sasfal}'
            f'\n **Validade da Guia**: 30 dias '
            f'\n **Contatos**: 3371-2116 / 3371-2117')

    if message.content.startswith('/examespardini'):
        ler_arquivo_xls(nome_arquivo)
        await message.channel.send(texto_arquivo)

    if message.content.startswith('/configesmeralda'):
        await message.channel.send('Aguarde a configuração')
        executar_script_vbs(caminho_script)


client.run(TOKEN)
