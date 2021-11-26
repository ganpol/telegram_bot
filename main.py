import telebot
from config import keys, TOKEN
from utils import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


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

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len != 3:
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values

    total_base = CurrencyConverter.convert(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()
