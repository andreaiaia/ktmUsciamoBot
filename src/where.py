from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

keyboard = [
  [ # First row
    InlineKeyboardButton("Option 1", callback_data='1'),
    InlineKeyboardButton("Option 2", callback_data='2'),
  ],
  [ # Second row
    InlineKeyboardButton("Option 3", callback_data='3')
  ]
]

reply_markup = InlineKeyboardMarkup(keyboard)

update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, _: CallbackContext) -> None:
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=f"Selected option: {query.data}")