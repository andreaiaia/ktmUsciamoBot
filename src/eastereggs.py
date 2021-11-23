from telegram import Update
from telegram.ext import CallbackContext
from src.helpers import (get, put)


def dna(update: Update, context: CallbackContext) -> None:
  key = str(update.message.chat.id) + '-' + str(update.message.from_user.id)
  value = 0
  if get(key, context):
    value = int(get(key, context))
  value += 1
  put(key, value, context)
  update.message.reply_text(f"Bidoni di Dna: {str(value)}.")
