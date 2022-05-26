import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS

@Client.on_message(filters.command(["اذاعة"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**❃ يتم بدأ الاذاعة الان ❃**")
        if not message.reply_to_message:
            await wtf.edit("**- يجب عليك الرد على الرسالة التي تريد اذاعتها**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**جار الاذاعة**\n\n*الارسال الى:** `{sent}` **من الدردشات** \n**خطا في ارسال الى :** `{failed}` **من الدردشات**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"**تمت الاذاعة**\n\n**تم بنجاح الارسال الى:** `{sent}` **من الدردشات** \n**خطا في ارسال الى :** `{failed}` **من الدردشات**")
