import telebot

TOKEN = ' '

bot = telebot.TeleBot(TOKEN)

keys = {
    'Рубль': 'RUB',
    'Доллар': 'USD',
    'Евро': 'EURO',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введине команду боту в следующем формате:\n' \
           '<имя валюты> <в какую валюты перевести> <кол-во переводимой валюты>\
           Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
        bot.reply_to(message, text)


bot.polling()
