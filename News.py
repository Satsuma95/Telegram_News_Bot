import time
import random
import requests
import telebot
from confug import *

AXTUNG = telebot.TeleBot(TOKENT)

slavianskii_zashim_slovarem = dict()
slovar = dict()
slovaa = []

@AXTUNG.message_handler(commands=['start'])
def start(message):
    AXTUNG.send_message(message.chat.id, "Н/А")
    AXTUNG.send_sticker(message.chat.id, "CAACAgIAAxkBAAELaNtlzjbdEGTKv-xxVTTDWKuo5HiDRgACShsAAo9-CUkFx6SkNGB_jjQE")

@AXTUNG.message_handler(commands=['News'])
def news(message):
    user_mes = message.text.split("/News")[1].strip()
    api(user_mes)

def api(user_mes):
    url = f"https://newsapi.org/v2/everything?q={user_mes}&language=ru&apiKey={API}"
    request_result = requests.get(url)
    JS = request_result.json()
    al = JS["articles"]
    for x in al:
        print(x["description"],x["title"],x["url"])
        break

api("Майнкрафт")

@AXTUNG.message_handler(content_types=['text'])
def text(message):
    pass


AXTUNG.polling()


"""
ОЧЕНЬ МНОГО ДОМАШКИ!!!!! ОСТОРОЖНО!!

1. Юзер вводит: "/news роблокс", нужно отловить всё то, что он написал после самой команды и поместить в переменную
2. Данные отправить по ссылке точно также, как и мы делали в функции locatio или get_city_image в прошлом проекте
3. Получить всё с сайта и в красивом виде отправить пользователюы"""