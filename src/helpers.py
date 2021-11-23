import sys
from telegram import Update
from telegram.ext import CallbackContext

def simple_reply(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(
      chat_id=update.effective_chat.id, text=get_msg(update.message.text))

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

def put(key, value, context):
    # how to make a key: 
    # str(update.message.chat.id) + '-' + str(update.message.from_user.id)
    # Store value
    context.chat_data[key] = value


def get(key, context):
    # Load value and send it to the user
    return context.chat_data.get(key, False)

