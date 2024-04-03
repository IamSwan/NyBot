import discord
from discord.ext import commands

class Nybot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self):
        print("Bot is ready.")

    async def on_message(self, message):
        author: discord.Member = message.author
        if author == self.user:
            return
        if type(author) == discord.User:
            return
        if author.guild_permissions.manage_messages:
            return
        if ".com" in message.content or ".net" in message.content or ".org" in message.content or ".gg" in message.content:
            await message.delete()

    def run(self, token):
        super().run(token)
