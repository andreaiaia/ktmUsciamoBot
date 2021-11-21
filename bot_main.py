import logging
from telegram import (
    Update,  
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler, 
    CallbackQueryHandler
)
from src.helpers import (get_msg, btn_join, get, put)

# Insert your token, you can have one from the BotFather
TOKEN = "YOUR TOKEN HERE"

def simple_reply(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg(update.message.text))

def hangout(update: Update, _: CallbackContext) -> None:
  keyboard = [
      [InlineKeyboardButton("IO CI SONO", callback_data='1')]
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text(get_msg('/hangout'), reply_markup=reply_markup)

def main():
  # Create the Updater and pass the Token
  updater = Updater(TOKEN, use_context=True)
  # Create a dispatcher variable for ease
  dp = updater.dispatcher
  # This prints error's log to help with debug
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      level=logging.INFO)

  # Create the commands and add them to the dispatcher queue
  # text commands (the ones with the /)
  
  # Basic commands - starting and using the bot
  dp.add_handler(CommandHandler('start', simple_reply))
  dp.add_handler(CommandHandler('help', simple_reply))
  dp.add_handler(CommandHandler('wiki', simple_reply))

  # Hangouts making
  dp.add_handler(CommandHandler('usciamo', hangout))
  dp.add_handler(CallbackQueryHandler(btn_join))

  dp.add_handler(CommandHandler('put', put))
  dp.add_handler(CommandHandler('get', get))

  # Inline keyboard commands (the ones you can call with @)
  
  # Start the bot
  updater.start_polling()
  # Run the bot until user presses Crtl-C or SIGINT, SIGTERM or SIGABRT
  updater.idle()

if __name__ == '__main__':
  main()