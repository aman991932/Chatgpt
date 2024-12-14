from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from .db import db
from pyrogram import Client, filters
from info import ADMINS

@Client.on_message(filters.private & filters.command("users") & filters.user(ADMINS))
async def users(bot, update):
    total_users = await db.total_users_count()
    text = "Bot Status\n"
    text += f"\nTotal Users: {total_users}"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )
  
