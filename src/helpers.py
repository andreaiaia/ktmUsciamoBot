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
  

def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]

    # Store value
    context.chat_data[key] = value
    # Send the key to the user
    update.message.reply_text(key)


def get(update, context):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = context.args[0]

    # Load value and send it to the user
    value = context.chat_data.get(key, 'Not found')
    update.message.reply_text(value)
