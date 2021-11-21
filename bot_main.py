from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging

# Inserire il proprio token ottenuto dal BotFather
TOKEN = "INSERISCI IL TUO TOKEN"

def start(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Benvenuto in ktmUsciamoBot, io sono qui per aiutare voialtri ad organizzarvi per uscire. \n Usa il comando /help per vedere la lista di ciò che posso fare.")

def echo(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update: Update, context: CallbackContext):
  text_caps = ' '.join(context.args).upper()
  context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def inline_caps(update: Update, context: CallbackContext):
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
  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      level=logging.INFO)
  
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

  echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

  caps_handler = CommandHandler('caps', caps)
  dispatcher.add_handler(caps_handler)

  inline_caps_handler = InlineQueryHandler(inline_caps)
  dispatcher.add_handler(inline_caps_handler)

  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()