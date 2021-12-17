from telegram import (
    Update,
    InputTextMessageContent,
    InlineQueryResultArticle
)
from telegram.ext import CallbackContext
from src.helpers import get_msg, put, get


def hangout(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    put(key, "", context)
    update.message.reply_text(get_msg('/hangout'))


def join(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    folks = get(key, context)
    if folks == "aborted" or folks == False:
        text = get_msg('/join_failed_reply')
    else:
        new_folk = str(update.message.from_user.username)
        folks = f"{folks} @{new_folk}"
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
    # TODO fare la leaderboard degli orari proposti
    key = f"{str(update.effective_chat.id)}-time"

    msg = (update.message.text).split()     # msg contiene l'orario proposto
    leaderboard = get(key, context)

    if (leaderboard == False):
        newLeaderboard = {f"{msg[1]}": 1,}
    else:
        newLeaderboard = leaderboard
        if msg[1] in newLeaderboard.keys():
            newLeaderboard[msg[1]] += 1
        else:
            newLeaderboard[msg[1]] = 1

    put(key, newLeaderboard, context)
    
    meeting_time = most_upvoted(newLeaderboard)

    text = f"{get_msg('/when')}{meeting_time}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def summary(update: Update, context: CallbackContext) -> None:
    key = f"{str(update.effective_chat.id)}-hangout"
    folks = get(key, context)
    text = "Non si fa nulla per ora, sorry not sorry."

    if folks != "aborted" and folks != False:
        text = f"Per ora siamo {folks}."

    loc_key = f"{str(update.effective_chat.id)}-location"
    location = get(loc_key, context)
    if location != "aborted" and location != False:
        text = f"{text}\nDovremmo andare a {location}."
    
    time_key = f"{str(update.effective_chat.id)}-time"
    time = get(time_key, context)
    if time != "aborted" and time != False:
        text = f"{text}\nCi vediamo alle {time}."
    
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)


def most_upvoted(times):
    winner = {"time": "0", "val": 0}
    for i in times:
        if times[i] >= winner["val"]:
            winner["time"] = i
            winner["val"] = times[i]
    
    return winner["time"]