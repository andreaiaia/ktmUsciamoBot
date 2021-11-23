import sys
from uuid import uuid4
from telegram import (
  Update
)
from telegram.ext import (
  Updater,
  CallbackContext,
  CommandHandler
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
  

def put(key, value, context):
    # key = str(update.message.chat.id) + '-' + str(update.message.from_user.id)
    # Store value
    context.chat_data[key] = value


def get(key, context):
    # key = str(update.message.chat.id)
    # Load value and send it to the user
    return context.chat_data.get(key, False)

