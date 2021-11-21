import sys
from telegram import (
  Update,
  InlineQueryResultArticle,
  InputTextMessageContent,
  ParseMode,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  CallbackQuery
)
from telegram.ext import (
  CallbackContext,
  CommandHandler,
  InlineQueryHandler,
  CallbackQueryHandler,
)

def get_msg(command):
  parent = sys.path[0]
  f = open(f"{parent}/texts{command}.txt", "r")
  text = f.readlines()
  f.close()
  msg = ""
  for line in text:
    msg = msg + line
  return msg

def btn_join(update: Update, context: CallbackContext) -> None:
  print(update.callback_query.from_user.username) # the username
  query = update.callback_query
  query.answer()
  # usando query.data, scopri come ottenere il nick di chi c'è e aggiungilo alla lista
  
