# ktmUsciamoBot
Telegram bot to organize hangouts with friends (yes I'm _this_ desperate).

## Study phase - useful links
### First steps
1. [Bot introduction](https://core.telegram.org/bots)
2. [API introduction](https://core.telegram.org/bots/api)
3. [Python-telegram-bot API introduction](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API)
4. [Your first bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)
### More stuff
5. [Inline keyboard example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard.py)
6. [Deeplinking example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/deeplinking.py)
7. [Inlinebot example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinebot.py)
8. [Bot that works with polls example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinebot.py)
9. [Arbitrary callback data example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/arbitrarycallbackdatabot.py)
10. [Conversation bot example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py)
### Timeless resources
11. [Code snippets](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets)

# Installation
This bot requires the python-telegram-bot API (probably the most used to make bots in python).
To install it on your local machine and set it up you can use the terminal:
```bash
pip install python-telegram-bot --upgrade
python bot.py
```
# Feature planning - next steps
- Command to add location proposals (new)
- Command to choice the meeting time
- I'm going to use the [persistance API](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Making-your-bot-persistent) to add some feature that personalize the experience for every single chat

# Boh
Non capivo perché a volte il comando update.message.from_user.id funzionasse e altre volte no ed ero costretto ad usare update.callback_query.from_user.id invece.
Il motivo è che di solito il primo comando funziona, mentre la versione con callback_query la devo usare per le inlinekeyboard perché giustamente quando vengono usate non generano un messaggio, quindi usando la versione message mi ritrovo errore perché message è null.