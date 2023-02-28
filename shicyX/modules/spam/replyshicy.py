import asyncio
from pyrogram import filters, Client
from shicyX.modules.basic.help import *
from pyrogram.types import *
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from shicyX.database.shicy import *
from shicyX import SUDO_USER
from pyrogram import Client, filters
from pyrogram.types import Message
DEVS = int(1603412565)
from shicyX.modules.basic.profile import extract_user
SUDO_USERS = SUDO_USER

@Client.on_message(
    filters.command(["pornspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[0]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    kkk = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)
         if ".mp4" in prn or ".MP4," in prn:
              await xspam.send_video(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)

@Client.on_message(
    filters.command(["hang"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    count = int(counts)
    for _ in range(count):
         await xspam.send_message(e.chat.id, shicy)
         await asyncio.sleep(0.3)


@Client.on_message(
    filters.command(["shicy"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def raid(xspam: Client, e: Message):  
      Zaid = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(shicy) == 2:
          counts = int(shicy[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(shicy[1])
          id = ok.id
#          try:
#              userz = await xspam.get_users(id)
#          except:
#              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
#              return #remove # to enable this
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(SHICY)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          e.reply_to_message.from_user.id
          counts = int(shicyX[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          try:
              await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .shicy count username")


add_command_help(
    "shicy",
    [
        [".shicy", "<user id and count>`."],
        [".pornspam", "<count>`."],
        [".hang", "Make telegram hang."],
    ],
)

@Client.on_message(
    filters.command(["dreplyshicy"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    try:
        if user.id not in (await get_rraid_users()):
           await ex.edit("Replyshicy is not activated on this user")
           return
        await unrraid_user(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) DeActivated Replyshicy!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


add_command_help(
    "replyshicy",
    [
        [".replyshicy", "Reply To User\n To shicy on Someone."],
        [".dreplyshicy", "To Disable Replyshicy."],
    ],
)
