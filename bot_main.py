import logging
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from telegram import (
    Update, 
    InlineQueryResultArticle, 
    InputTextMessageContent,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler, 
    InlineQueryHandler,
    CallbackQueryHandler
)
from src.helpers import get_msg, btn_join

# Insert your token, you can have one from the BotFather
TOKEN = "INSERISCI IL TOKEN"

def start(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('start'))

def help(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('help'))

def wiki(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('help'))

def hangout(update: Update, _: CallbackContext) -> None:
  keyboard = [
      [InlineKeyboardButton("IO CI SONO", callback_data='1')]
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text(get_msg('hangout'), reply_markup=reply_markup)

def main():
  # Create the Updater and pass the Token
  updater = Updater(TOKEN, use_context=True)
  # Create a dispatcher variable for ease
  dispatcher = updater.dispatcher
  # This prints error's log to help with debug
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      level=logging.INFO)

  # Create the commands and add them to the dispatcher queue
  # text commands (the ones with the /)
  
  # Basic commands - starting and using the bot
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)
  help_handler = CommandHandler('help', help)
  dispatcher.add_handler(help_handler)
  wiki_handler = CommandHandler('wiki', wiki)
  dispatcher.add_handler(wiki_handler)

  # Hangouts making
  hangout_handler = CommandHandler('usciamo', hangout)
  dispatcher.add_handler(hangout_handler)
  dispatcher.add_handler(CallbackQueryHandler(btn_join))

  # Inline keyboard commands (the ones you can call with @)
  
  # Start the bot
  updater.start_polling()
  # Run the bot until user presses Crtl-C or SIGINT, SIGTERM or SIGABRT
  updater.idle()

if __name__ == '__main__':
  main()