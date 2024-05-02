import json
import time
import random
import requests
import telebot
from confug import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

AXTUNG = telebot.TeleBot(TOKENT)

slavianskii_zashim_slovarem = dict()
slovar = dict()
slovaa = []

@AXTUNG.message_handler(commands=['start'])
def start(message)->None:
    knopki = InlineKeyboardMarkup()
    fstart0 = InlineKeyboardButton("Новости", callback_data="News")
    fstart1 = InlineKeyboardButton("Связь с разрабом", callback_data="Help")
    knopki.add(fstart0,fstart1)
    AXTUNG.send_animation(message.chat.id,"https://i.pinimg.com/originals/da/3f/9e/da3f9e8270a5453f98f0830aaf6cf852.gif",caption="Этот бот может выдать свежии новости по темам которые вам интересуют",reply_markup=knopki)
    AXTUNG.send_sticker(message.chat.id, "CAACAgIAAxkBAAELaNtlzjbdEGTKv-xxVTTDWKuo5HiDRgACShsAAo9-CUkFx6SkNGB_jjQE")

@AXTUNG.callback_query_handler(func=lambda call: call.data == "News")
def inli(call)->None:
    res = AXTUNG.send_message(call.from_user.id,"валяй какие новости хочешь")
    AXTUNG.register_next_step_handler(res,news)

@AXTUNG.callback_query_handler(func=lambda call: call.data == "Help")
def inli(call)->None:
    resh = AXTUNG.send_message(call.from_user.id,"подавай жалобу")
    AXTUNG.register_next_step_handler(resh,otsiv)

def news(message)->None:
    ret = api(message.text)
    if len(ret)>0:
        AXTUNG.send_message(message.chat.id, text=ret)
    else:
        print ("404")

def otsiv(message)->None:
    me = message.text
    yj = read("y.json")
    yj.append({"text":me})
    write("y.json",yj)
    AXTUNG.forward_message(admin,message.from_user.id,message.message_id)
def read(name)->list:
    with open(f"{name}", 'r', encoding="UTF-8") as f:
        js = json.load(f)
        return js
def write(name,dannie)->None:
    with open(name, 'w', encoding="UTF-8") as fuile:
        json.dump(dannie, fuile, ensure_ascii=False)


def api(user_mes)->str:
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

смысл такой:
/send 34873847 привет, как дела? -  эту строчку разделить на команду сенд, айдишник и сам текст (нужен будет сплит)
после чего просто отправить сообщение челу по айдишнику (отправить сообщение)

задание, прям как в ньюс делали, аналогично


"""