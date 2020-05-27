import telebot
import config
from telebot import types



bot = telebot.TeleBot(config.TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna = types.KeyboardButton('Author')
itembtnb = types.KeyboardButton('Hello!')
itembtnc = types.KeyboardButton('Мои данные')
markup.row(itembtnc)
markup.row(itembtna)
markup.row(itembtnb)


@bot.message_handler(commands=['start', 'help'])
@bot.edited_message_handler(content_types=['text'])
def welcome(message):
    bot.send_sticker(message.chat.id, config.STICKER_ID)
    bot.send_message(message.chat.id, 'Добро пожаловать!')
    bot.send_message(message.chat.id, "Выбери одну из кнопок:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def usser(message):
    if 'Мои данные' in message.text:
        bot.send_message(message.chat.id, 'Your name:' + ' ' + str(message.chat.first_name))
        bot.send_message(message.chat.id, 'Your username:' + ' ' + '@' + str(message.chat.username))
        bot.send_message(message.chat.id, 'Your id:' + ' ' + str(message.chat.id))
    else:
        if 'Hello!' in message.text:
            bot.send_sticker(message.chat.id, config.STICKER_ID2)
        else:
            if 'Author' in message.text:
                bot.send_message(message.chat.id, '@maxA0n')
            return


bot.polling(timeout=60)
