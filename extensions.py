import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            quote_base = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'http://api.currencylayer.com/live?access_key=e312102310f35d5c9a003ab5c877a889&currencies={quote_tiker}&format={quote_base}')
        total_base = float(json.load(r.content)['quotes'][quote_tiker]) * amount

        return round(total_base, 3)
