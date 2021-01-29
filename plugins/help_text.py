import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import script

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["help"]))
def help_user(bot, update):

    bot.send_message(
        chat_id=update.chat.id,
        text=script.HELP_USER,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="JOIN OUR CHANNEL", url="https://t.me/Doraemon_Tamil")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["start"]))
def send_start(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=script.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="OFFICIAL CHANNEL , url="https://t.me/Doraemon_Tamil")], [InlineKeyboardButton(text="SUPPORT Group", url="https://t.me/DoraemonTamil"),
                                                    InlineKeyboardButton(text="CHANNEL", url="http://t.me/TamilAll_Contents")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["upgrade"]))
def upgrade(bot, update):

    bot.send_message(
        chat_id=update.chat.id,
        text=script.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@Client.on_message(filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=script.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    ) 
        
                