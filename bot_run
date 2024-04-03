#!/usr/bin/env python3

from src.nybot import Nybot
import dotenv
import os


if __name__ == "__main__":
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")

    bot = Nybot()
    bot.run(TOKEN)
