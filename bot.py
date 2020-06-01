import telebot
import config
from telebot import types



bot = telebot.TeleBot(config.TOKEN)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
buton1 = types.KeyboardButton('Назад 🔙')
itembtna = types.KeyboardButton('Разработчик')
itembtnb = types.KeyboardButton('Hello!')
itembtnc = types.KeyboardButton('Узнать свои данные')
markup1.row(itembtnc, itembtna)
markup1.row(itembtnb)
markup2.row(buton1)


@bot.message_handler(commands=['start', 'help'])
@bot.edited_message_handler(content_types=['text'])
def welcome(message):
    bot.send_sticker(message.chat.id, config.STICKER_ID)
    bot.send_message(message.chat.id, 'Добро пожаловать {name}, рад тебя видеть!'.format(name=message.chat.first_name))
    bot.send_message(message.chat.id, "Выбери одну из кнопок:", reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def usser(message):
    if 'Узнать свои данные' in message.text:
        bot.send_message(message.chat.id, 'Твоё имя:' + ' ' + str(message.chat.first_name))
        bot.send_message(message.chat.id, 'Твой username:' + ' ' + '@' + str(message.chat.username))
        bot.send_message(message.chat.id, 'Твой id:' + ' ' + str(message.chat.id), reply_markup=markup2)
    if 'Hello!' in message.text:
        bot.send_sticker(message.chat.id, config.STICKER_ID2, reply_markup=markup2)
    if 'Разработчик' in message.text:
        bot.send_message(message.chat.id, 'Напиши мне если тебя что-то интересует @maxA0n',
                         reply_markup=markup2)
    if 'Назад 🔙' in message.text:
        bot.send_message(message.chat.id, 'Выбери одну из кнопок:', reply_markup=markup1)


bot.polling(timeout=60)
