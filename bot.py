import os
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))
telebot.apihelper.proxy = {'https':os.getenv("PROXY")}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(chat_id=os.getenv("BOT_NAME"), text="Hello world!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(chat_id=os.getenv("BOT_NAME"), text=message.text)


bot.polling()
