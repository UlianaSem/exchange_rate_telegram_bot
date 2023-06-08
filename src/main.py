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
HELP = """Приветствую! Вам доступно две команды:
/help - для вывода этой справки,
/get - для получения курса валюты относительно рубля. Команда вводится в формате "/get валюта". Например, /get USD"""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def get_help(message):
    """Отправляет справку в чат пользователю
    :param message: сообщение пользователя"""
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['get'])
def main(message):
    """Отправляет курс в чат пользователю
    :param message: сообщение пользователя"""
    currency = src.utils.get_currency(message)
    rates_dictionary = src.utils.get_exchange_rate(URL, HEADERS, PARAMS)
    rate = src.utils.get_desired_currency(rates_dictionary, currency)
    answer_for_user = src.utils.check_in_file(currency, rate, rates_dictionary, PATH_TO_FILE)

    bot.send_message(message.chat.id, answer_for_user)


bot.polling(none_stop=True)
