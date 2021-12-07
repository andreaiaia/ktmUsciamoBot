from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle
)
from telegram.ext import CallbackContext
from src.helpers import get_msg, put, get


def hangout(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("IO CI SONO", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(get_msg('/hangout'), reply_markup=reply_markup)
    key = f"{str(update.effective_chat.id)}-hangout"
    put(key, "", context)


def inline_hangout(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    if not query:
        return
    results = []
    # Qui aggiungo gli orari tra cui scegliere
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Hangout',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def join(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    folks = get(key, context)
    if folks == "aborted" or folks == False:
        text = get_msg('/join_failed_reply')
    else:
        new_folk = str(update.message.from_user.username)
        folks = f"@{new_folk} {folks}"
        put(key, folks, context)
        text = f"Per ora ci sono: {folks}."
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def abort(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    put(key, "aborted", context)
    text = get_msg('/abort')
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)


def when(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('/when'))


def summary(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    folks = get(key, context)
    text = "Non si fa nulla per ora, sorry not sorry."

    if folks != "aborted" and folks != False:
        text = f"Per ora siamo {folks}."

    loc_key = f"{str(update.effective_chat.id)}-location"
    location = get(loc_key, context)
    print(location)
    if location != "aborted" and location != False:
        text = f"{text}\nDovremmo andare a {location}."
    
    time_key = f"{str(update.effective_chat.id)}-time"
    time = get(time_key, context)
    if time != "aborted" and time != False:
        text = f"{text}\nCi vediamo alle {time}."
    
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)
