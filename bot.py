import os
import time
import telebot
import html_parser

bot = telebot.TeleBot(os.getenv("TOKEN"))
telebot.apihelper.proxy = {'https': os.getenv("PROXY")}


intros = ["Добрый вечер. Список новых объявлений за сегодня:\n", "", "", "", ""]


def run():
    new_discussions = html_parser.get_new_discussions()
    html_parser.save_discussions()
    if new_discussions:
        bot.send_message(chat_id=os.getenv("CHAT_ID"),
                         text=str(new_discussions))


run()
