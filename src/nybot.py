import discord
from discord.ext import commands
import time
import threading

class Nybot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self):
        print("Bot is ready.")

    async def on_message(self, message):
        author: discord.Member = message.author
        if author == self.user:
            return

        if author.id == 657263582685298728 and message.content == "stop.":
            await message.channel.send("Stopping bot.")
            await self.close()

        if type(author) == discord.User:
            return
        if author.guild_permissions.manage_messages:
            return
        if ".com" in message.content or ".net" in message.content or ".org" in message.content or ".gg" in message.content:
            self.add_warn(author.id)
            await message.delete()
            if self.check_warns(author.id):
                await message.channel.send(f"{author.mention} has been warned 5 times.")
                await author.kick(reason="Bot flagged you.")
                return

    def get_user(self, user_id):
        return self._users[user_id]

    def get_data_base(self):
        return self._data_base

    def add_user(self, user):
        self._data_base.write(f"{user.id}: 0\n")

    def add_warn(self, user_id):
        print("Adding warn.")
        file = open("data_base.txt", "r")
        data = file.read()
        file.close()
        if not str(user_id) in data:
            file.close()
            file = open("data_base.txt", "a")
            file.write(f"{user_id}: 1\n")
            return
        for line in data.split("\n"):
            if line.startswith(str(user_id)):
                data = data.replace(f"{user_id}: {int(line.split()[1])}", f"{user_id}: {int(line.split()[1]) + 1}")
                break
        file = open("data_base.txt", "w")
        file.write(data)
        file.close()

    def check_warns(self, user_id):
        file = open("data_base.txt", "r")
        data = file.read()
        file.close()
        for line in data.split("\n"):
            if line.startswith(str(user_id)):
                if int(line.split()[1]) >= 5:
                    return True
        return False

    def reset_warns(self):
        while True:
            if super().is_closed():
                break
            time.sleep(5)
            print("Resetting warns.")
            file = open("data_base.txt", "r")
            data = file.read()
            file.close()
            for line in data.split("\n"):
                if len(line) == 0:
                    continue
                user_id = line.split()[0]
                data = data.replace(f"{user_id} {int(line.split()[1])}", f"{user_id} 0")
            file = open("data_base.txt", "w")
            file.write(data)
            file.close()

    def run(self, token):
        threading.Thread(target=self.reset_warns).start()
        super().run(token)
