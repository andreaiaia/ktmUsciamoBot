import sys
from telegram import Update
from telegram.ext import CallbackContext

def simple_reply(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(get_msg(update.message.text), parse_mode="MarkdownV2")

def get_msg(command):
    parent = sys.path[0]
    f = open(f"{parent}/texts{command}.md", "r")
    text = f.readlines()
    f.close()
    msg = ""
    for line in text:
        msg = msg + line
    return msg

def btn_join(update: Update, _: CallbackContext) -> None:
    print(update.callback_query.from_user.username) # the username
    query = update.callback_query
    query.answer()

def put(key, value, context) -> None:
    # how to make a key: 
    # str(update.message.chat.id)
    # Store value
    context.chat_data[key] = value

def get(key, context):
    # Load value and send it to the user
    return context.chat_data.get(key, False)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text="Non posso farlo questo, AO le hai lette le istruzioni? Usa /help o /wiki.")
