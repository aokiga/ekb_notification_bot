import os
import time
import telebot
import html_parser

bot = telebot.TeleBot(os.getenv("TOKEN"))
telebot.apihelper.proxy = {'https': os.getenv("PROXY")}

SLEEPING_TIME = 5


def run():
    while (True):
        new_discussions = html_parser.get_new_discussions()
        html_parser.save_discussions()
        if new_discussions:
            bot.send_message(chat_id=os.getenv("CHAT_ID"),
                             text=str(new_discussions))
        time.sleep(SLEEPING_TIME)


run()
