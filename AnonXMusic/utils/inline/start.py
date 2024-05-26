from pyrogram.types import InlineKeyboardButton
import config
from AnonXMusic import app

def start_panel(localized_text):
    buttons = [
        [
            InlineKeyboardButton(
                text=localized_text["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=localized_text["S_B_2"], 
                url=config.SUPPORT_CHAT
            ),
        ],
    ]
    return buttons

def private_panel(localized_text):
    buttons = [
        [
            InlineKeyboardButton(
                text=localized_text["S_B_3"], 
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(
                text=localized_text["S_B_4"], 
                callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text=localized_text["S_B_5"], 
                user_id=config.OWNER_ID
            ),
            InlineKeyboardButton(
                text=localized_text["S_B_2"], 
                url=config.SUPPORT_CHAT
            ),
        ],
        [
            InlineKeyboardButton(
                text=localized_text["S_B_6"], 
                url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text=localized_text["S_B_7"], 
                url="https://telegra.ph/file/c45acbf0c5107a79952c7.mp4"
            ),
        ],
    ]
    return buttons
