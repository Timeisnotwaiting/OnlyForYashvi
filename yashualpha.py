from pyrogram import Client, filters
from pyrogram.filters import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import *

YASHUALPHA = [5296178757, 5285667393, 5432903250, 1985209910, 5429087029]

YashuAlpha = Client(":Yashvi:", API_ID, API_HASH, BOT_TOKEN)

@YashuAlpha.on_message(filters.command("kiss", "") & filters.user(YASHUALPHA))
