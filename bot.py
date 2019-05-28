import os
import sys
import telebot
import html_parser

bot = telebot.TeleBot(os.getenv("TOKEN"))
SITE_URL = "обсуждения.екатеринбург.рф"

intro_new = """Добрый вечер.
Список новых обсуждений за сегодня:
"""

intro_all = """Добрый вечер.
Напоминаем, что в данный момент доступны следущие обсуждения:
"""


def send_discussions(getter, greeter):
    discussions = getter()
    if discussions:
        message_text = greeter + '\n' + \
            '\n\n'.join(map('\n{}'.format(SITE_URL).join, discussions))
        bot.send_message(chat_id=os.getenv("CHAT_ID"), text=message_text)


def send_all_discussions():
    send_discussions(html_parser.get_discussions, intro_all)


def send_new_discussions():
    send_discussions(html_parser.get_new_discussions, intro_new)


if __name__ == "__main__":
    if sys.argv[1] == '--new':
        send_new_discussions()
    else:
        send_all_discussions()
    html_parser.save_discussions()
