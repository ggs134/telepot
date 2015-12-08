# -*- coding: utf-8 -*-
#import sys
import time
import pprint
import telepot
import requests
import json

def handle(msg):
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    #pprint.pprint(msg)
    #print type(msg)
    rMessage = msg['text']
    fromID = msg['from']['id']
    oID = 33612976
    f = open('tellyou.jpg','rb')
    bot.sendMessage(oID, msg['from']['first_name'].encode('utf-8')+" 가 조회를 했군\n"+str(time.asctime()))
    usage = "안녕 여러분ㅎ \n조회를 원해? \n1.목표조회 : getObject \n 2.조직조회 : getDepartment \n 3.조직-목표 조회 : getDeptObj \n ** 대소문자 주의!"
    show_keyboard = {'keyboard': [['명령어조회','getObject'], ['getDepartment','getDeptObj']]}

    if rMessage == "getObject":
        res = requests.get('http://192.168.1.19:5000/object')
        bot.sendMessage(fromID, res.text)
        return
    elif rMessage == "getDepartment":
        res = requests.get('http://192.168.1.19:5000/department')
        bot.sendMessage(fromID, res.text)
        return
    elif rMessage == "getDeptObj":
        res = requests.get('http://192.168.1.19:5000/dept-obj')
        bot.sendMessage(fromID, res.text)
        return
    
    #bot.sendPhoto(fromID, f)
    bot.sendMessage(fromID, usage, reply_markup=show_keyboard)
    f.close() 

# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
#TOKEN = sys.argv[1]
TOKEN = "155578772:AAGngKO2rPtjzC2_P3CM7FSsL-FIAfzRk8A"

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Listening ...'

# Keep the program running.
while 1:
        time.sleep(10)
