import sys
from telegram import Update
from telegram.ext import CallbackContext
from src.helpers import (get, put)

def dna(update: Update, context: CallbackContext) -> None:
    key = str(update.message.from_user.id)
    value = 0
    if get(key, context):
        value = int(get(key, context))
    value += 1
    put(key, value, context)
    update.message.reply_text(f"Bidoni di Dna: {str(value)}.")

def ping(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("PONG.")

def angry(update: Update, _: CallbackContext) -> None:
    parent = sys.path[0]
    pic = f"{parent}/img/violence.jpg"
    update.message.reply_photo(photo = open(pic, 'rb'))

def badum(update: Update, _: CallbackContext) -> None:
    parent = sys.path[0]
    media = f"{parent}/img/tsss.mp3"
    update.message.reply_audio(audio = open(media, 'rb'))