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



@tree.command(name="announce", description="Announce a message to the announcements channel.")
@app_commands.describe(
    message = "The message you want to announce.",
    category = "The category of the announcement."
)

async def announce(
        interaction: discord.Interaction,
        message: str,
        category: str,
        ping: bool = False
    ):
    if interaction.user.guild_permissions.send_messages == False:
        await interaction.response.send_message("You do not have permission to send messages in the <#1263276734007087127> channel.", ephemeral=True)
        return
    if ping:
        await client.get_channel(1263276734007087127).send("@everyone")
    await client.get_channel(1263276734007087127).send(
    embed=discord.Embed(
        title = category,
        description = message,
        color = discord.Color.dark_purple()
    ))
    await interaction.response.send_message("Your message has been sent! :)", ephemeral=True)


client.run(TOKEN)
