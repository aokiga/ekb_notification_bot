import os
import time
import random
import telebot
import html_parser

bot = telebot.TeleBot(os.getenv("TOKEN"))
telebot.apihelper.proxy = {'https': os.getenv("PROXY")}

intros = ["Добрый вечер.\nСписок новых обсуждений за сегодня:\n"]


def run():
    new_discussions = html_parser.get_new_discussions()
    html_parser.save_discussions()
    if new_discussions:
        message_text = intros[random.randint(0, len(intros) - 1)] + '\n' + '\n\n'.join(
            map(lambda a: '\nобсуждения.екатеринбург.рф'.join(a), new_discussions))
        bot.send_message(chat_id=os.getenv("CHAT_ID"), text=message_text)


run()
