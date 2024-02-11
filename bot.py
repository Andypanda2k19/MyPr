import time

import telebot
from telebot import types

bot = telebot.TeleBot('6869103546:AAGAG2AhyMAgAuzZrVBxeldgoAwQeaR2pTk')


@bot.message_handler(commands = ['start'])
def get_rasp(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Расписание занятий', callback_data='rowspis')
    markup.add(btn1)
    bot.send_message(message.chat.id, "🍲 Привет! Я Ваш верный помощник в расписании предметов, а так же другой полезной информации.", reply_markup = markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def allrow_rasp(callback):
    if callback.data == 'rowspis':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='🍲 Понедельник', callback_data='day1')
        btn2 = types.InlineKeyboardButton(text='🍲 Вторник', callback_data='day2')
        btn3 = types.InlineKeyboardButton(text='🍲 Среда', callback_data='day3')
        btn4 = types.InlineKeyboardButton(text='🍲 Четверг', callback_data='day4')
        btn5 = types.InlineKeyboardButton(text='🍲 Пятница', callback_data='day5')
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(chat_id = callback.message.chat.id, text = 'Выберите день недели',reply_markup=markup)

    if callback.data == 'day1':
        file = open('1.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, '🍲 Понедельник')
        bot.delete_message(callback.message.chat.id, callback.message.id)
    if callback.data == 'day2':
        file = open('2.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, '🍲 Вторник')
        bot.delete_message(callback.message.chat.id, callback.message.id)
    if callback.data == 'day3':
        file = open('3.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, '🍲 Среда')
        bot.delete_message(callback.message.chat.id, callback.message.id)
    if callback.data == 'day4':
        file = open('4.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, '🍲 Четверг')
        bot.delete_message(callback.message.chat.id, callback.message.id)
    if callback.data == 'day5':
        file = open('5.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, '🍲 Пятница')
        bot.delete_message(callback.message.chat.id, callback.message.id)

bot.polling(none_stop=True, interval=0)