import requests
import tornado.web
import signal
BOT_TOKEN = '1233523210:AAG5pf7YRlPpuIcuOoB6c5ycDwEJ-v1WGjE'
URL = "http://api.telegram.org/bot%s/" % BOT_TOKEN
# encoding: utf8


import urllib as urllib2
import time
import json
import sys

from poster3.encode import multipart_encode
from poster3.streaminghttp import register_openers

import subprocess



API = 'http://api.telegram.org/bot'
TOKEN = '1233523210:AAG5pf7YRlPpuIcuOoB6c5ycDwEJ-v1WGjE'
PAVEL = '609959297'

URL = API + TOKEN


# noinspection PyPep8Naming
def getUpdates():
    get = URL + '/getUpdates'
    response = urllib2.urlopen(get)
    return response.read()


INVALID_UPDATE_ID = 0

global last_update_id
last_update_id = INVALID_UPDATE_ID


def getCommand():
    js = json.loads(getUpdates())

    update_obj = js['result'][-1]

    global last_update_id
    if last_update_id == INVALID_UPDATE_ID:
        last_update_id = update_obj['update_id']
        return None

    if update_obj['update_id'] != last_update_id:
        last_update_id = update_obj['update_id']
        return update_obj['message']['text']
    return None


def sendMessage(chat_id, text):
    sendMessage = {
        'chat_id': chat_id,
        'text': text
    }
    get = URL + '/sendMessage?' + urllib.urlencode(sendMessage)
    response = urllib2.urlopen(get)


def sendPhoto(chat_id, image_file):
    register_openers()
    values = {
        'chat_id': chat_id,
        'photo': open(image_file, 'rb')
    }
    data, headers = multipart_encode(values)
    request = urllib2.Request(URL + '/sendPhoto?', data, headers)
    response = urllib2.urlopen(request)


# bot = Bot(TOKEN)
# bot.sendMessage(PAVEL, 'Тест бота')
# sys.exit(0)

while True:
    command = getCommand()
    if None != command:

        if 'screenshot' == command:
            sendMessage(PAVEL, 'Щас сделаю, погодь')
            time.sleep(1)
            subprocess.Popen(['import', '-window', 'root', 'screenshot.png'])
            time.sleep(3)
            sendPhoto(PAVEL, 'screenshot.png')
            time.sleep(1)
            sendMessage(PAVEL, 'Поймал???')

        if 'damn' == command:
            sendMessage(PAVEL, "Нахуй пошёл!!!")

    time.sleep(1)
