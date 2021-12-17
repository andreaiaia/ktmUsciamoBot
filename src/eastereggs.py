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

def sendPic(update: Update, _: CallbackContext) -> None:
    parent = sys.path[0]
    pic = f"{parent}/img{(update.message.text)}.jpg"
    update.message.reply_photo(photo = open(pic, 'rb'))

def sendAudio(update: Update, _: CallbackContext) -> None:
    parent = sys.path[0]
    media = f"{parent}/img{(update.message.text)}.mp3"
    update.message.reply_audio(audio = open(media, 'rb'))

def sendGif(update: Update, _: CallbackContext) -> None:
    parent = sys.path[0]
    media = f"{parent}/img{(update.message.text)}.gif"
    update.message.reply_animation(animation = open(media, 'rb'))