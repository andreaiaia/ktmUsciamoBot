from telegram import (
    Update,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import CallbackContext
from src.helpers import get_msg


def hangout(update: Update, _: CallbackContext) -> None:
  keyboard = [
      [InlineKeyboardButton("IO CI SONO", callback_data='1')]
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text(get_msg('/hangout'), reply_markup=reply_markup)
