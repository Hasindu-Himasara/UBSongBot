#Uvindu Bro <https://t.me/UvinduBro>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm 🎼 ᴍᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ 🎧

🌷 jυѕт ѕend мe тнe ѕong naмe yoυ wanт тo download.
🌷 Ex-:```/song Alone```

🌷 **Inbox & Groups Supported**
♻️ **24 Hour Active**

"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="☘ Join ☘", url="https://t.me/SLStockMusic"
                    ),
                    InlineKeyboardButton(
                        text="🎧 Støck Mυѕιc 🎧", url="https://t.me/SLStockMusic"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ Music Downloader Bot is online.")
idle()
