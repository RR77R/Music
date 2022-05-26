import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["بحث"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("- يجب عليك كتابه عنوان مع الامر للبحث")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**⪼ جار البحث انتظر قليلا**")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"العنولن - {results[i]['title']}\n"
            text += f"المدة - {results[i]['duration']}\n"
            text += f"المشاهدات - {results[i]['views']}\n"
            text += f"القناة - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
