import logging
from telegram import Update, KeyboardButton
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    InlineQueryHandler
)
from src.hangoutMaking import hangout, join, abort, summary
from src.helpers import simple_reply, unknown
from src.eastereggs import dna, ping, sendPic, sendAudio, sendGif

# Insert your token, you can have one from the BotFather
TOKEN = "TOKEN"

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
    dp.add_handler(CommandHandler('join', join))

    # Comandi meta per l'hangout making
    dp.add_handler(CommandHandler('abort', abort))
    dp.add_handler(CommandHandler('quindi', summary))

    # Easter eggs
    dp.add_handler(CommandHandler('dna', dna))
    dp.add_handler(CommandHandler('ping', ping))
    dp.add_handler(CommandHandler('violence', sendPic))
    dp.add_handler(CommandHandler('badum', sendAudio))
    dp.add_handler(CommandHandler('grosso', sendGif))
    dp.add_handler(CommandHandler('shesaid', sendGif))


    # TESTING AREA
    # some_strings = ["col1", "col2", "row2"]
    # button_list = [[KeyboardButton(s)] for s in some_strings]
    # build_menu(button_list, 2)

    # Invalid command handler - this MUST be the last handler
    dp.add_handler(MessageHandler(Filters.command, unknown))
    # Start the bot
    updater.start_polling()
    # Run the bot until user presses Crtl-C or SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()