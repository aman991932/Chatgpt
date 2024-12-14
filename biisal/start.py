from pyrogram import Client, filters, enums
from .db import db
import random
from Script import script
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from info import *

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    rm = InlineKeyboardMarkup(
        [[
	    InlineKeyboardButton('𝐀𝐕 𝐁𝐎𝐓𝐙 𝐔𝐏𝐃𝐀𝐓𝐄 🤖', url='https://t.me/AV_BOTz_UPDATE')
	],[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ', url="https://t.me/AV_SUPPORT_GROUP"),
            InlineKeyboardButton("❤️‍🩹 ᴀʙᴏᴜᴛ", callback_data='about')
        ]] 
    )
    await message.reply_photo(photo=START_IMG, caption=script.START_TXT.format(message.from_user.mention),
        reply_markup=rm,
        parse_mode=enums.ParseMode.HTML
    )
    return

@Client.on_callback_query()
async def cb_handler(client: Client, update: CallbackQuery):
    if update.data == "close_data":
        await update.message.delete()
    elif update.data == "about":
        buttons = [[
		InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/BOT_OWNER26')
	],[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔒 Cʟᴏsᴇ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        me2 = (await client.get_me()).mention
        await update.message.edit_text(
            text=script.AMAN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)


    elif update.data == "start":
        buttons = [[
	    InlineKeyboardButton('𝐀𝐕 𝐁𝐎𝐓𝐙 𝐔𝐏𝐃𝐀𝐓𝐄 🤖', url='https://t.me/AV_BOTz_UPDATE')
	],[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ', url="https://t.me/AV_SUPPORT_GROUP"),
            InlineKeyboardButton("❤️‍🩹 ᴀʙᴏᴜᴛ", callback_data='about')
        ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.message.edit_text(
            text=f"""<b>ʜᴇʏ {update.from_user.mention} 👋, \n\nɪ ᴀᴍ <a href='https://t.me/AV_IMA_TO_URL_BOT'>ɪᴍᴀɢᴇ ᴛᴏ ʟɪɴᴋ</a> ʙᴏᴛ ɪᴜꜱᴛ ꜱᴇɴᴅ ᴛᴏ ʏᴏᴜʀ ɪᴍᴀɢᴇ & ᴠɪᴅᴇᴏ ᴀɴᴅ 𝟻 ᴍʙ.\n\nMʏ Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/AV_MOVIE_HOUSE'>ᴀᴠ ʙᴏᴛᴢ</a></b>""",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
