"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(f'Привет, друг! Введи название планеты на английском, например '
                              f'/planet Sun, Mercury, Venus, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto!')


ddef planet_constellation(update, context):
    input_planet = update.message.text.split()[-1].capitalize()

    planets = {'Sun': ephem.Sun,
              'Mercury': ephem.Mercury,
              'Venus': ephem.Venus,
              'Moon': ephem.Moon,
              'Mars': ephem.Mars,
              'Jupiter': ephem.Jupiter,
              'Saturn': ephem.Saturn,
              'Uranus': ephem.Uranus,
              'Neptune': ephem.Neptune,
              'Pluto': ephem.Pluto,
              }
    if input_planet.capitalize() in planets:
        planet = planets[input_planet](date.today().strftime('%y/%m/%d'))
        const = ephem.constellation(planet)
        update.message.reply_text(f'Сегодня {input_planet} находится в созвездии {const[-1]}.')
    else:
        update.message.reply_text('Такой планеты нет в солнечной системе, повтори ввод.')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
