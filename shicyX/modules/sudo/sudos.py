from pyrogram import Client, filters
from pyrogram.types import Message
DEVS = int(1603412565)
from shicyX.modules.basic.profile import extract_user
from shicyX import SUDO_USER
from config import OWNER_ID
from shicyX.modules.basic.help import add_command_help

ok = []


@Client.on_message(filters.command("sudolist", ".") & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (SUDO_USER)
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("No Users have been set yet")
    gban_list = "**Sudo Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i}`\n"
    return await ex.edit(gban_list)


@Client.on_message(filters.command("addsudo", ".") & filters.user(OWNER_ID))
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`sabar kentodd Gw lagi Galau`")
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
        return await ex.edit("**yaaa okeey 🐶**")

    try:
        if user.id in SUDO_USER:
            return await ex.edit("`User already gmuted`")
        SUDO_USER.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Added To Sudo Users!")
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return



add_command_help(
    "sudos",
    [
        [
            "addsudo <reply/username/userid>",
            "Add any user as Sudo (Use This At your own risk maybe sudo users can control ur account).",
        ],
        ["rmsudo <reply/username/userid>", "Remove Sudo access."],
        ["sudolist", "Displays the Sudo List."],
    ],
)
