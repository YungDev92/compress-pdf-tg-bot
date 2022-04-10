from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('CHAT GROUP', url='t.me/YdpDiscussion'),
            InlineKeyboardButton('CHANNEL', url='t.me/YdpBots')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/YdpDiscussion'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
