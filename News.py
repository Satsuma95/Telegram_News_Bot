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
    ret = api(user_mes)
    if len(ret)>0:
        AXTUNG.send_message(message.chat.id, text=ret)
    else:
        print ("404")



def api(user_mes):
    url = f"https://newsapi.org/v2/everything?q={user_mes}&language=ru&apiKey={API}"
    request_result = requests.get(url)
    JS = request_result.json()
    al = JS["articles"]
    finmes = ""
    for x in al:
        mes = x["description"],x["title"],x["url"]
        sum_one_news = len(mes[0]) + len(mes[1]) + len(mes[2])
        if len(finmes)+sum_one_news<4096:
            finmes += (f"{mes[1]}\n{mes[0]}\n{mes[2]}\n\n")
        else:
            print ("404 2")


    return finmes


@AXTUNG.message_handler(content_types=['text'])
def text(message):
    pass


AXTUNG.polling()


"""
сделать функционал, по которому можно будет отправлять сообщение пользователю
смысл такой:
/send 34873847 привет, как дела? -  эту строчку разделить на команду сенд, айдишник и сам текст
после чего просто отправить сообщение челу по айдишнику. если всё будет ок, то сделать тоже самое в обратную сторону
/send_adm привет, го в сэтисфектори??!!?!?!
и всё сообщение должно улететь тебе :)


"""