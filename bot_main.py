import logging
from telegram import Update, ParseMode
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler, 
    CallbackQueryHandler
)
from src.hangoutMaking import hangout, join, abort, summary
from src.helpers import (simple_reply, btn_join)
from src.eastereggs import dna, ping

# Insert your token, you can have one from the BotFather
TOKEN = "YOUR TOKEN HERE"

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
  dp.add_handler(CommandHandler('join', join))
  dp.add_handler(CommandHandler('abort', abort))
  dp.add_handler(CommandHandler('quindi', summary))

  # Easter eggs
  dp.add_handler(CommandHandler('dna', dna))
  dp.add_handler(CommandHandler('ping', ping))

  # Inline keyboard commands (the ones you can call with @)
  
  # Start the bot
  updater.start_polling()
  # Run the bot until user presses Crtl-C or SIGINT, SIGTERM or SIGABRT
  updater.idle()

if __name__ == '__main__':
  main()