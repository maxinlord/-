import telebot
import config
from telebot import types
import requests


bot = telebot.TeleBot('1267177588:AAGN2MrqeG694G723-z8NdqlvhM9xfMuxpA')

@bot.message_handler(content_types=['sticker'])
def test(message):
    bot.send_message(message.chat.id, {file_id}.__format__(file_id=sticker))


bot.polling(timeout=60)