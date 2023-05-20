import telebot

bot = telebot.TeleBot("6237928184:AAGL69utLeIJe_jZxqI_ecUf8ccFkLq1dU0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def handle_docs_audio(message):
    text = message.text
    if 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}')

bot.polling()