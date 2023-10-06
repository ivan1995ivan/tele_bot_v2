import webbrowser

import telebot


bot = telebot.TeleBot('6599601001:AAF4taeCDIShAZmkbaKnXm6ReyLXBXtrMGY')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://google.com')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    if last_name:
        bot.send_message(message.chat.id, f'Privet !, {first_name} {last_name} !')
    else:
        bot.send_message(message.chat.id, f'Privet ! {first_name} !')
    # bot.send_message(message.chat.id, f'Privet, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        # bot.send_message(message.chat.id, f'Privet, {message.from_user.first_name} {message.from_user.last_name}')
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name

            if last_name:
                bot.send_message(message.chat.id, f'Privet !, {first_name} {last_name} !')
            else:
                bot.send_message(message.chat.id, f'Privet ! {first_name} !')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')




bot.polling(none_stop=True)