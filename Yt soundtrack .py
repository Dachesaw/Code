import telebot
from telebot import types
bot = telebot.TeleBot('5543889798:AAHx-yuvJMTjvRG5DPS-k6_zr6BaOB9UEk4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, please send url')
    





bot.polling(none_stop=True)