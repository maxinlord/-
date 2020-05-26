import telebot
import config
import pickle
import requests
import random
from telebot.types import Message

bot = telebot.TeleBot(config.TOKEN)
USER = set()


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    bot.send_sticker(message.chat.id, config.STICKER_ID)
    bot.send_message(message.chat.id,'Добро пожаловать!')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo(message):
    if 'Author' in message.text:
        bot.send_message(message.chat.id,'@maxA0n')
        return
    bot.send_message(message.chat.id, 'Your name:' + ' ' + str(message.chat.first_name))
    bot.send_message(message.chat.id, 'Your username:' + ' ' + '@' + str(message.chat.username))
    bot.send_message(message.chat.id, 'Your id:' + ' ' + str(message.chat.id))
    USER.add(message.from_user.id)


bot.polling(timeout=60)
