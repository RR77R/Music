import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
import requests
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import IMG, BOT_TOKEN, CHANNEL

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
do = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
    if do.count("left") or do.count("Bad Request: user not found"):
        keyboard03 = [[InlineKeyboardButton("- اضغط للاشتراك", url='https://t.me/{CHANNEL}')]]
        reply_markup03 = InlineKeyboardMarkup(keyboard03)
        await message.reply_text('-عذࢪأ ، عليك الاشتࢪاك في قناة البوت اولا .',
                                 reply_markup=reply_markup03)
    else:
    await message.reply_photo(
        photo= f"{IMG}" or "https://telegra.ph/file/b178d8f486c1b085cdb6a.jpg",
        caption=f"""**اهلا بك عزيزي في بوت الميوزك 
وظيفة البوت لتشغيل المقاطع الصوتية في المجموعات يجب عليك اضاف هذا البوت وارسل امر  !انضمام """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/jmthon")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command("الاوامر") & filters.group & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5f3af650e4c26e68287a8.jpg",
        caption=f"""**❃ اوامر الاعضاء في المجموعة ❃**

`!تشغيل`
- اكتب الامر مع العنوان او بالرد على عنوان او بالرد على مقطع MP3 لتشغيل المقطع الصوتي في الاتصال

`!تحميل`
- اكتب الامر مع عنوان المقطع لتحميله على صيغه MP3

`!بحث`
- اكتب الامر مع عنوان للبحث عنه وارسال لك معلومات من اليوتيوب

**❃ اوامر مشرفين المجموعه ❃**

`!ايقاف`
- لأيقاف المقطع المشغل مؤقتا فقط ارسل الامر

`!تخطي`
- لعمل تخطي للمقطع المشغل الحالي وتشغيل الذي يليه

`!انهاء`
- لانهاء التشغيل والخروج من المكالمة الصوتية

`!انضمام`
- لانضمام الحساب المساعد للدردشة فقط ارسل الامر في الكروب""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/jmthon")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )


