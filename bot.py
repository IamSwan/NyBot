#!/bin/env python3

import discord
from discord import app_commands
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Bot is ready.")
    await tree.sync()

@tree.command(name="test")
async def test(interaction: discord.Interaction, message: str):
    await client.get_channel(1263276734007087127).send(message)
    await interaction.response.send_message("Your message has been sent! :)")


client.run(TOKEN)
