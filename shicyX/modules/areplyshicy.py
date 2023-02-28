from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from shicyX.database.shicy import *
from shicyX import SUDO_USER
from pyrogram import Client, filters
from pyrogram.types import Message
DEVS = int(1694909518)
from shicyX.modules.basic.profile import extract_user
SUDO_USERS = SUDO_USER



@Client.on_message(
    filters.command(["replyshicy"], ".") & (filters.me | filters.user(SUDO_USER))
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
    if user.id == client.me.id:
        return await ex.edit("**Okeh .. ✨**")
    elif user.id == SUDO_USERS:
        return await ex.edit("**Okay But Failed Because this user in sudos.. 👑**")
    elif user.id == VERIFIED_USERS:
        return await ex.edit("**Chal Chal Baap ko Mat sikha.. 👑**")
    try:
        if user.id in (await get_rraid_users()):
           await ex.edit("shicyReplay  is activated on this user")
           return
        await karman_user(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Activated ReplyKarman!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return
