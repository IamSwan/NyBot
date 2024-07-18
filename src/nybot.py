import discord
from discord.ext import commands
import time
import threading

class Nybot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self):
        print("Bot is ready.")

    def run(self, token):
        super().run(token)
