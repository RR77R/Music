import requests
from pyrogram import idle
from pyrogram import Client, filters
from pyrogram.types import Message

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

Client.join_chat("-1001325518787")
bot.start()
run()
idle()
