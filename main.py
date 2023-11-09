from Client import Client
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

@Bot.on_message(filters.incoming)
async def inline_handlers(_, event: Message):
    if event.text == '/start':
        return
    answers = f'**📂 Rᴇsᴜʟᴛs Fᴏʀ ➠ {event.text} \n\n➠ Tʏᴘᴇ Oɴʟʏ Mᴏᴠɪᴇ Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ.✍️\n➠ Aᴅᴅ Yᴇᴀʀ Fᴏʀ Bᴇᴛᴛᴇʀ Rᴇsᴜʟᴛ.🗓️\n➠ Jᴏɪɴ @MOVIES_VILLA_UPDATE\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**'
    async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):
        if message.text:
            thumb = None
            f_text = message.text
            msg_text = message.text.html
            if "|||" in message.text:
                f_text = message.text.split("|||", 1)[0]
                msg_text = message.text.html.split("|||", 1)[0]
            answers += f'**🍿 Tɪᴛʟᴇ ➠ ' + '' + f_text.split("\n", 1)[0] + '' + '\n\n📜 Aʙᴏᴜᴛ ➠ ' + '' + f_text.split("\n", 2)[-1] + ' \n\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\nLɪɴᴋ Wɪʟʟ Aᴜᴛᴏ Dᴇʟᴇᴛᴇ Iɴ 𝟼𝟶Sᴇᴄ...⏰\n\n**'
    try:
        msg = await event.reply_text(answers)
        await asyncio.sleep(65)
        await event.delete()
        await msg.delete()
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Fᴀɪʟᴇᴅ ᴛᴏ Aɴsᴡᴇʀ - {event.from_user.first_name}")

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
