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
import settings # Импорт скрытых ключей из папки settings
import ephem # Модуль для расчета положения небесного тела
from datetime import datetime 
from pprint import pprint

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

date_str = datetime.now().strftime("%Y-%d-%m")

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Введите текст который хотите получить обратно'
    print(text)
    update.message.reply_text(text)

def planet_user(update, context):

    message_dict = update.message.text.split(' ')
    planet_name = message_dict[-1] # Получение название планеты из сообщения пользователя
    planet_list= [name for _0, _1, name in ephem._libastro.builtin_planets()] # Список планет доступных для отслеживания

    wrong_name_planet = 'Такого небесного тела нет, выбирете одно из достпуных' # Переменная с выводом в случае не нахождения планеты в списке

    for x in planet_list:  # Проверка на наличие введенной планеты в списке доступных
        if planet_name == x:
            wrong_name_planet = x # Перезапись переменной на название прошедшей проверку планеты


    if planet_name == '/planet':                    # Если введена только команда /planet, выводится: 'К команде /planet добавьте название планеты'
        text = 'К команде /planet добавьте название небесного тела'
        update.message.reply_text(text) # Вывод в консоль 'К команде /planet добавьте название планеты'
        update.message.reply_text(planet_list) # Вывод в пользовательский чат списка планет
        print(text) # Вывод в консоль 'К команде /planet добавьте через пробел название планеты'
        pprint(planet_list) # Вывод в консоль списка доступных планет

    elif planet_name == wrong_name_planet: # Проверка на соответствие полученного имени из введенного пользователем и правильно перезаписанной переменной wrong_name_planet
        planet = getattr(ephem, planet_name) # Склейка названия планеты и модуля ephem для получения типа ephem.Mars
        planet_final = planet(date_str) # Подготовка переменной для constellation. date_str - текущее время 
        constellation = ephem.constellation(planet_final)
        constellation_final = f"Небесное тело {planet_name} находится в созвездии {constellation}"
        update.message.reply_text(constellation_final) # Вывод расчетов constellation в чат пользователя
        print(constellation_final) # Вывод расчетов constellation в консоль

    else:
        update.message.reply_text(wrong_name_planet) # Если нет ни одного совпадания с написанным пользователем
        print(wrong_name_planet)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher                                    # Используется диспетчер для того, чтобы при наступлении события вызывалась наша функция
    dp.add_handler(CommandHandler("start", greet_user))      # CommandHandler обработка команд
    dp.add_handler(CommandHandler("planet", planet_user))    # Реакция бота на команду в чате Телеграма
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # MessageHandler - обработка типа сообщения
                                                             # Filters.text - реакция только на текстовые сообщения
    logging.info('Start bot')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
