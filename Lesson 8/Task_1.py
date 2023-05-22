import telebot
import requests
import time
from telebot import types

bot = telebot.TeleBot("")

markup = types.ReplyKeyboardMarkup(row_width=2)
btn_reg = types.KeyboardButton('регистрация')
btn_att = types.KeyboardButton('оповещение')
markup.add(btn_reg, btn_att)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):    
    bot.send_message(message.from_user.id, "Howdy, how are you doing?", reply_markup = markup)

@bot.message_handler(content_types=['text'])
def text_message(message):    
    data = open('log.txt', mode='a', encoding='utf-8')
    text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
    data.write(text)
    data.close()
    if message.text == 'регистрация':
        reg_data = open('registered_users.txt', mode='r+', encoding='utf-8')
        id_list = reg_data.readlines()   
        print(id_list)     
        if f'{message.from_user.id}\n' not in id_list:            
            reg_data.write(f'{message.from_user.id}\n')
            reg_data.close()
            bot.reply_to(message, 'Регистрация прошла успешно')
        else:
            bot.reply_to(message, 'Вы уже зарегистрированы')
        reg_data.close()
    elif message.text == 'оповещение':
        reg_data = open('registered_users.txt', mode='r+', encoding='utf-8')
        id_list = reg_data.read().split('\n')
        reg_data.close()
        id_list = id_list[:-1]
        for id in id_list:            
            bot.send_message(id, 'совещание через 5 минут')

bot.polling()