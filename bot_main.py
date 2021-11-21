from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging
from src.helpers import get_msg

# Insert your token, you can have one from the BotFather
TOKEN = "2094326543:AAFFhZREiRK51eujOED-BWHgz2gxA9tf6yM"

def start(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('start'))

def help(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('help'))

def wiki(update: Update, context: CallbackContext) -> None:
  context.bot.send_message(chat_id=update.effective_chat.id, text=get_msg('help'))

def inline_caps(update: Update, context: CallbackContext) -> None:
  query = update.inline_query.query
  if not query:
    return
  results = []
  results.append(
    InlineQueryResultArticle(
      id=query.upper(),
      title='caps',
      input_message_content=InputTextMessageContent(query.upper())
    )
  )
  context.bot.answer_inline_query(update.inline_query.id, results)


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
  
  # Comandi base - introduzione al bot
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)
  help_handler = CommandHandler('help', help)
  dispatcher.add_handler(help_handler)
  wiki_handler = CommandHandler('wiki', wiki)
  dispatcher.add_handler(wiki_handler)

  # Inline keyboard commands (the ones you can call with @)
  inline_caps_handler = InlineQueryHandler(inline_caps)
  dispatcher.add_handler(inline_caps_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until user presses Crtl-C or SIGINT, SIGTERM or SIGABRT
  updater.idle()

if __name__ == '__main__':
  main()