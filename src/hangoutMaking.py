import threading
from telegram import (
    Update,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import CallbackContext
from src.helpers import get_msg, put, get

def hangout(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("IO CI SONO", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(get_msg('/hangout'), reply_markup=reply_markup)
    key = f"{str(update.message.chat.id)}-hangout"
    put(key, "", context)
    timeout = threading.Timer(7200, expired) # 2 hours timeout
    timeout.start()

def join(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.message.chat.id)}-hangout"
    if get(key, context) == "":
        folks = get(key, context)
        newFolk = str(update.message.from_user.username)
        folks = f"@{newFolk} {folks}"
        put(key, folks, context)
        text = f"Per ora ci sono: {folks}."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=text)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=get_msg('/join_failed_reply'))

def expired(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.message.chat.id)}-hangout"
    if get(key, context) == "":
        abort(update, context)

def abort(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.message.chat.id)}-hangout"
    put(key, "aborted", context)
    text = get_msg('/abort')
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)

def summary(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.message.chat.id)}-hangout"
    folks = get(key, context)
    text = "Non si fa nulla per ora, sorry not sorry."
    text2 = ""
    text3 = ""

    if folks != "aborted" and folks != False:
        text = f"Per ora siamo {folks}."

    loc_key = f"{str(update.message.chat.id)}-location"
    location = get(loc_key, context)
    if location != "aborted" and folks != False:
        text = f"{text}\nDovremmo andare a {location}."
    
    time_key = f"{str(update.message.chat.id)}-time"
    time = get(time_key, context)
    if time != "aborted" and folks != False:
        text = f"{text}\nCi vediamo alle {time}."
    
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)
        