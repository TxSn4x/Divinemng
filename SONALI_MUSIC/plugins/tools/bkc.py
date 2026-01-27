import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SONALI_MUSIC import app
from config import SUPPORT_CHAT

BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT)]])

RAND = "https://files.catbox.moe/tehyii.mp4"
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LESBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LESBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

#test

NEXI_VID = [

"https://files.catbox.moe/du8ylb.mp4", 
]



def handle_action(client, message: Message, action: str, action_name: str):
    sender = message.from_user
    sender_name = f"[{sender.first_name}](tg://user?id={sender.id})" 

    if message.reply_to_message:
        replied_user = message.reply_to_message.from_user
        replied_user_name = f"[{replied_user.first_name}](tg://user?id={replied_user.id})"
        msg = f"{sender_name} sent a {action_name} to {replied_user_name}! {message.reply_video(
                random.choice(NEXI_VID),}"
    else:
        msg = f"{sender_name} sent a {action_name} to themselves! {action_info[action]['emoji']}"

    response = requests.get(action_info[action]message.reply_video(
                random.choice(NEXI_VID))
    if response.status_code == 200:
        gif_link = response.json()["url"]
        client.send_animation(message.chat.id, animation=gif_link, caption=msg, parse_mode="markdown")



#test

@app.on_message(filters.command("rand"))
async def rand(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    RAND = f"**🍷** {mention} **ɪꜱ** {mm}**% ʀᴀɴᴅ!**"
    await message.reply_text(RAND, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("horny"))
async def horny(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    HORNY = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ!**"
    await message.reply_text(HORNY, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("gay"))
async def gay(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    GAY = f"**🍷** {mention} **ɪꜱ** {mm}**% ɢᴀʏ!**"
    await message.reply_text(GAY, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("lesbian"))
async def lezbian(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    FEK = f"**💜** {mention} **ɪꜱ** {mm}**% ʟᴇsʙɪᴀɴ!**"
    await message.reply_text(FEK, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("boob"))
async def boob(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    BOOBS = f"**🍒** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}**!**"
    await message.reply_text(BOOBS, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("cock"))
async def cock(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    COCK = f"**🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ**"
    await message.reply_text(COCK, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)


@app.on_message(filters.command("cute"))
async def cute(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    CUTE = f"**🍑** {mention} {mm}**% ᴄᴜᴛᴇ**"
    await message.reply_text(CUTE, reply_markup=BUTTON, disable_web_page_preview=True, quote=True)
