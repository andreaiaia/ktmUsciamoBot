from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
import logging

# Inserire il proprio token ottenuto dal BotFather
TOKEN = "INSERISCI IL TOKEN"

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      level = logging.INFO)

def start(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Benvenuto in ktmUsciamoBot, io sono qui per aiutare voialtri ad organizzarvi per uscire. \n Usa il comando /help per vedere la lista di ciò che posso fare.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()