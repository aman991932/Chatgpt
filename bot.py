# ©️biisal jai shree krishna 😎
from pyrogram import Client
from info import *


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="AMAN VISHVAKARMA 😂😂🤣🤣",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "biisal"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(ADMINS, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️😅😅😅__**")


Bot().run()
