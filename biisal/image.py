import asyncio, requests, os
from pyrogram import Client, filters
from pyrogram.types import *
from .fsub import get_fsub
from info import *

def upload_image_requests(image_path):
    upload_url = "https://envs.sh"

    try:
        with open(image_path, 'rb') as file:
            files = {'file': file} 
            response = requests.post(upload_url, files=files)

            if response.status_code == 200:
                return response.text.strip() 
            else:
                raise Exception(f"Upload failed with status code {response.status_code}")

    except Exception as e:
        print(f"Error during upload: {e}")
        return None

@Client.on_message(filters.media & filters.private)
async def upload(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    file_size_limit = 10 * 1024 * 1024  # 10 MB in bytes
    if message.document and message.document.file_size > file_size_limit:
        await message.reply_text("<b>⚠️ ꜱᴇɴᴅ ᴀ ᴍᴇᴅɪᴀ ᴜɴᴅᴇʀ 𝟷𝟶 ᴍʙ</b>")
        return
    elif message.photo and message.photo.file_size > file_size_limit:
        await message.reply_text("<b>⚠️ ꜱᴇɴᴅ ᴀ ᴍᴇᴅɪᴀ ᴜɴᴅᴇʀ 𝟷𝟶 ᴍʙ</b>")
        return

    path = await message.download()

    uploading_message = await message.reply_text("<code>ᴜᴘʟᴏᴀᴅɪɴɢ...</code>")

    try:
        image_url = upload_image_requests(path)
        if not image_url:
            raise Exception("Failed to upload file.")
    except Exception as error:
        await uploading_message.edit_text(f"Upload failed: {error}")
        return

    try:
        os.remove(path)
    except Exception as error:
        print(f"Error removing file: {error}")
        
    await uploading_message.delete()
    codexbots=await message.reply_photo(
        photo=f'{image_url}',
        caption=f"<b>ʏᴏᴜʀ ᴄʟᴏᴜᴅ ʟɪɴᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ 👇</b>\n\n𝑳𝒊𝒏𝒌 :-\n<code>{image_url}</code> \n\n<b>ʙʏ - <a href='https://t.me/AV_BOTz_UPDATE'>ᴀᴠ ʙᴏᴛᴢ ᴜᴘᴅᴀᴛᴇ</a></b>",
        #disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(text="• ᴏᴘᴇɴ ʟɪɴᴋ •", url=image_url),
            InlineKeyboardButton(text="• sʜᴀʀᴇ ʟɪɴᴋ •", url=f"https://telegram.me/share/url?url={image_url}")
        ], [
            InlineKeyboardButton(text="❌   ᴄʟᴏsᴇ   ❌", callback_data="close_data")
        ]])
                                      )

