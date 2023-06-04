import os
import telebot
import src.utils


URL = "https://api.apilayer.com/exchangerates_data/latest"
PARAMS = {
  'base': 'RUB'
}
HEADERS = {
  "apikey": os.environ.get('EXCHANGE_RATE_API_KEY')
}
PATH_TO_FILE = 'src/rate_data.json'
TOKEN = os.environ.get('EXCHANGE_RATE_BOT_API')


def main():
    """Задает алгоритм работы программы"""
    currency = input("Введите код валюты, курс которой хотите получить относительно рубля (например, USD)\n").strip()

    rates_dictionary = src.utils.get_exchange_rate(URL, HEADERS, PARAMS)
    rate = src.utils.get_desired_currency(rates_dictionary, currency)
    answer_for_user = src.utils.check_in_file(currency, rate, rates_dictionary, PATH_TO_FILE)
    print(answer_for_user)


if __name__ == "__main__":
    main()
