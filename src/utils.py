import json

import requests


def get_exchange_rate(url, headers, params):
    """
    Возвращает словарь с данными о курсе
    :param url: ссылка на apilayer
    :param headers: API токен
    :param params: параметры запроса (базовая валюта, относительно которой выводится курс)
    :return: словарь с данными о курсе
    """
    response = requests.request("GET", url, headers=headers, params=params)

    status_code = response.status_code
    if status_code == 200:
        result = response.json()
    else:
        result = None

    return result


def get_desired_currency(rates_dictionary, currency):
    """
    Возвращает курс необходимой валюты
    :param rates_dictionary: словарь с курсами валют
    :param currency: необходимая валюта
    :return: курс (float)
    """
    if rates_dictionary is None or currency is None:
        return None

    if rates_dictionary['rates'].get(currency) is not None:
        return rates_dictionary['rates'][currency]

    return None


def check_in_file(currency, rate, rates_dictionary, path_to_file):
    """
    Проверяет курс записанный в файле, и возвращает ответ об изменение курса в виде строки
    :param path_to_file: путь к файлу
    :param rates_dictionary: словарь с курсами валют
    :param currency: валюта
    :param rate: курс
    :return: ответ об изменение курса в виде строки
    """
    if rates_dictionary is None or currency is None or rate is None:
        return 'Ошибка запроса или нет информации о данной валюте. Проверьте ваш запрос и попробуйте еще раз.'

    with open(path_to_file, 'r') as file:
        file_text = file.read()

    rate_data_dictionary = json.loads(file_text)

    if currency in rate_data_dictionary['rates'] and rate != rate_data_dictionary['rates'][currency]:
        answer = f'Курс изменился, сейчас курс составляет {rate} {currency}'
        update_file(rates_dictionary, path_to_file)

    elif currency in rate_data_dictionary['rates'] and rate == rate_data_dictionary['rates'][currency]:
        answer = f'Курс не изменился и составляет {rate} {currency}'

    else:
        answer = 'Ошибка запроса или нет информации о данной валюте. Проверьте ваш запрос и попробуйте еще раз.'

    return answer


def update_file(rates_dictionary, path_to_file):
    """
    Обновляет файл с курсами валют
    :param path_to_file: путь к файлу
    :param rates_dictionary: словарь с курсами для записи
    """
    rates_string = json.dumps(rates_dictionary)

    with open(path_to_file, 'w') as file:
        file.write(rates_string)


def get_currency(user_request):
    """
    Возвращает требуемую валюту из запроса
    :param user_request: запрос пользователя
    :return: валюта для запроса
    """
    try:
        currency = user_request.text.strip().split()[1]
    except IndexError:
        currency = None

    return currency
