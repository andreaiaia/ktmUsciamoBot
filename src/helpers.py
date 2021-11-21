import sys
from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler
)

def get_msg(command):
  parent = sys.path[0]
  f = open(f"{parent}/texts/{command}.txt", "r")
  text = f.readlines()
  f.close()
  msg = ""
  for line in text:
    msg = msg + line
  return msg

def btn_join(update: Update, _: CallbackContext) -> None:
  query = update.callback_query
  query.answer()
  # usando query.data, scopri come ottenere il nick di chi c'è e aggiungilo alla lista
  query.edit_message_text(text=f"Hai scelto 'io ci sono'")
