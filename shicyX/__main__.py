import asyncio
import importlib
from pyrogram import idle
from shicyX.helper import join
from shicyX.modules import ALL_MODULES
from shicyX import clients, app, ids
from config import BOTLOG_CHATID

BOT_VER = "0.1.0"
CMD_HANDLER = ["."]
MSG_ON = """
⚡ **Pyrochiy Telah Hidup** ⚡
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Ngecek Sendiri Tod**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("shicyX.modules" + all_module)
        print(f"Successfully Imported {all_module} ✔")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} ✔ ")
            await cli.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
