from pyrogram import Client, filters
from pyrogram.filters import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import *
from random import choice

KISS = ["https://te.legra.ph/file/3bf7cc60c09e9c1f1ea81.jpg",
        "https://te.legra.ph/file/4b80e2a5fe1671bb3f951.jpg",
        "https://te.legra.ph/file/5865758b24bcedb3b582c.jpg"
       ]

MARKUP = [[
                InlineKeyboardButton("✅", callback_data="k_accept"),
                InlineKeyboardButton("❌", callback_data="k_reject"),
         ]]

YASHUALPHA = [5296178757, 5285667393, 5432903250, 1985209910, 5429087029]

YASHU = [5296178757, 5285667393, 5432903250]

ALPHA = [1985209910, 5429087029]

init = None

YashuAlpha = Client(":Yashvi:", API_ID, API_HASH, BOT_TOKEN)

@YashuAlpha.on_message(filters.command("kiss", "") & filters.user(YASHUALPHA))
async def kiss(_, m):
    global init
    init = m.from_user.id
    if not m.reply_to_message and not m.reply_to_message.from_user.id in YASHUALPHA:
        return 
    if m.from_user.id == YASHUALPHA[3] or m.from_user.id == YASHUALPHA[4]:
        await _.send_message(m.chat.id, "Alpha 💭 wants to kiss Yashu 💭", reply_markup=InlineKeyboardMarkup(MARKUP))
    else:
        await _.send_message(m.chat.id, "Alpha 💭 wants to kiss Yashu 💭", reply_markup=InlineKeyboardMarkup(MARKUP))

@YashuAlpha.on_callback_query(filters.regex("k_accept"))
async def cbquery(_, c: CallbackQuery):
    if c.data == "k_accept":
        if c.from_user.id == init:
            return await c.answer()
        if c.from_user.id not in YASHUALPHA:
            return await c.answer("This is only for YASHU-ALPHA !", show_alert=True)
        alpha_m = (await _.get_users(init)).mention
        yashu_m = (await _.get_users(c.from_user.id)).mention
        await c.message.reply_photo(choice(KISS), f"{yashu_m} {alpha_m}")
        await c.message.delete()
        await c.answer()
    elif c.data == "k_reject":
        if c.from_user.id == init:
            return await c.answer()
        if c.from_user.id not in YASHUALPHA:
            return await c.answer("This is only for YASHU-ALPHA !", show_alert=True)
        await c.message.delete()


YashuAlpha.run()
print("bot started !")
