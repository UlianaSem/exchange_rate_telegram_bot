import os
import telebot


URL = "https://api.apilayer.com/exchangerates_data/latest?base=RUB&date=1995-12-13"

params = {
  'base': 'RUB'
}
headers= {
  "apikey": os.environ.get('EXCHANGE_RATE_API_KEY')
}
