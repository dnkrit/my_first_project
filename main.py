import telebot
import datetime
import time
import threading
import random
bot = telebot.TeleBot('Введите Ваш Токен')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(messaqe, 'Привет! Я чат бот, который будет напоминать тебе пить водичку!')
    reminder.thread = threading.Thread(target= send_reminders, args= (message.chat.id))
    reainder.thread.start()


@bot.message_handler(commands=['facts'])
def fact_message(message):
    list = ["**Вода на Земле может быть старше самой Солнечной системы**"
            "**Исследования показывают,что от 38% до 58% воды в наиших океанах**"
            "**Горячая вода замерзает быстрое холодной**"]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови Факт о воде {random.fact}')


def send_reminders(chat_id):
    first.rem = "09:00"
    second.rem = "12:00"
    end.rem = "15:00"
    while True:
        now = datetime.datetime.now().strftime('%H,%M')
        if now == first.rem or now == second.rem or now == end.rem:
            bot.send_messaqe(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)
bot.polling(none_stop=True)