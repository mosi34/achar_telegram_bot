import telebot
import requests


bot_token = '986536837:AAFtNWYZ6fBnKHJWrNPLVPAf1SlvGbARhe0'
bot = telebot.TeleBot(token=bot_token)


def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome ')
    print(message)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'to use this bot send it a username')

# we work here


@bot.message_handler(commands=['dork'])
def dorking_google(message, *args):
    name = args[0]
    ext = args[1]
    command = 'intitle:"index of"/({},{})'.format(name, ext)

    bot.reply_to(message, 'to use this bot send it a username')


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))


bot.polling()
