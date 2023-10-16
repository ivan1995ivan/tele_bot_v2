import telebot
import sqlite3

bot = telebot.TeleBot('6599601001:AAF4taeCDIShAZmkbaKnXm6ReyLXBXtrMGY')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('telesql.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hello ! Now we register you')




bot.polling(none_stop=True)