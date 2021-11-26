import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise ConversionException(f'Невозможно перевести одинаковые валюты - {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Введена неправильная или несуществующая валюта - {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Введена неправильная или несуществующая валюта - {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Неправильно введено число {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price' +
                         f'?fsym={base_ticker}' +
                         f'&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]
        total_base *= amount

        return total_base
