import telebot

import schedule

import time

bot=telebot.TeleBot("1967626202:AAFykDZY-cKrU7UmOCkBxqTKAb97RxbTKCg")

i=0

imege="imeges/"+str(i)+".jpg"

chat_id="1202602736"

def imeges ():

  bot.send_message(chat_id , "ورد اليوم من الدراسة")

  img=open (imege , 'rb')

  bot.send_photo(chat_id, img)

def i ():

  i = i + 1

schedule.every().day.at("07:20:00").do(imeges)

schedule.every().day.at("17:30:01").do(i)

while True:

  schedule.run_pending()
