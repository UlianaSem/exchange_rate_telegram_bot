import pytest
import src.utils


@pytest.fixture
def get_rates_dict_for_test():
    return {'success': True, 'timestamp': 1686067863, 'base': 'RUB', 'date': '2023-06-06',
            'rates': {'AED': 0.04515, 'AFN': 1.064704, 'ALL': 1.234994, 'AMD': 4.757696,
                      'ANG': 0.02217, 'AOA': 7.489182, 'ARS': 2.989971, 'AUD': 0.01841, 'AWG': 0.022127,
                      'AZN': 0.020882, 'BAM': 0.02249, 'BBD': 0.024838, 'BDT': 1.327574, 'BGN': 0.022518,
                      'BHD': 0.004634, 'BIF': 34.725053, 'BMD': 0.012293, 'BND': 0.016593, 'BOB': 0.085001,
                      'BRL': 0.060329, 'BSD': 0.012302, 'BTC': 4.69744e-07,'BTN': 1.016226, 'BWP': 0.167485,
                      'BYN': 0.03105, 'BYR': 240.933107, 'BZD': 0.024796, 'CAD': 0.016485, 'CDF': 28.580071,
                      'CHF': 0.011154, 'CLF': 0.000355, 'CLP': 9.803765, 'CNY': 0.087528, 'COP': 52.277444,
                      'CRC': 6.622345, 'CUC': 0.012293, 'CUP': 0.325751, 'CVE': 1.267893, 'CZK': 0.270731,
                      'DJF': 2.190238, 'DKK': 0.085609, 'DOP': 0.673609, 'DZD': 1.681674, 'EGP': 0.379821,
                      'ERN': 0.184388, 'ETB': 0.672034, 'EUR': 0.011492, 'FJD': 0.027428, 'FKP': 0.009884,
                      'GBP': 0.009896, 'GEL': 0.032082, 'GGP': 0.009884, 'GHS': 0.138701, 'GIP': 0.009884,
                      'GMD': 0.731415, 'GNF': 105.780436, 'GTQ': 0.096315, 'GYD': 2.601767, 'HKD': 0.096417,
                      'HNL': 0.302588, 'HRK': 0.085363, 'HTG': 1.70992, 'HUF': 4.22861, 'IDR': 182.710884,
                      'ILS': 0.045454, 'IMP': 0.009884, 'INR': 1.014478, 'IQD': 16.114872, 'IRR': 520.280297,
                      'ISK': 1.72968, 'JEP': 0.009884, 'JMD': 1.90644, 'JOD': 0.008725, 'JPY': 1.715991,
                      'KES': 1.707381, 'KGS': 1.074382, 'KHR': 50.780129, 'KMF': 5.651477, 'KPW': 11.063677,
                      'KRW': 15.973616, 'KWD': 0.003782, 'KYD': 0.010251, 'KZT': 5.512335, 'LAK': 222.680525,
                      'LBP': 184.643147, 'LKR': 3.598421, 'LRD': 2.092101, 'LSL': 0.239953, 'LTL': 0.036297,
                      'LVL': 0.007436, 'LYD': 0.059439, 'MAD': 0.125362, 'MDL': 0.219332, 'MGA': 54.31036,
                      'MKD': 0.709654, 'MMK': 25.832781, 'MNT': 42.755238, 'MOP': 0.09936, 'MRO': 4.388422,
                      'MUR': 0.566658, 'MVR': 0.188813, 'MWK': 12.553476, 'MXN': 0.214034, 'MYR': 0.056638,
                      'MZN': 0.777499, 'NAD': 0.239948, 'NGN': 5.675207, 'NIO': 0.449961, 'NOK': 0.136192,
                      'NPR': 1.625961, 'NZD': 0.020212, 'OMR': 0.004733, 'PAB': 0.012302, 'PEN': 0.045308,
                      'PGK': 0.04365, 'PHP': 0.69004, 'PKR': 3.521571, 'PLN': 0.051479, 'PYG': 88.957219,
                      'QAR': 0.044751, 'RON': 0.057015, 'RSD': 1.347443, 'RUB': 1, 'RWF': 13.912789, 'SAR': 0.046097,
                      'SBD': 0.102533, 'SCR': 0.164456, 'SDG': 7.381686, 'SEK': 0.134027, 'SGD': 0.016571,
                      'SHP': 0.014957, 'SLE': 0.277549, 'SLL': 242.776979, 'SOS': 7.000569, 'SRD': 0.464626,
                      'STD': 254.430044, 'SVC': 0.107643, 'SYP': 30.885435, 'SZL': 0.236043, 'THB': 0.427162,
                      'TJS': 0.134332, 'TMT': 0.043024, 'TND': 0.038257, 'TOP': 0.029128, 'TRY': 0.264561,
                      'TTD': 0.083438, 'TWD': 0.377181, 'TZS': 29.108649, 'UAH': 0.454312, 'UGX': 46.007993,
                      'USD': 0.012293, 'UYU': 0.476754, 'UZS': 141.002251, 'VEF': 32574.74777, 'VES': 0.324884,
                      'VND': 288.750953, 'VUV': 1.476998, 'WST': 0.033853, 'XAF': 7.54293, 'XAG': 0.00052,
                      'XAU': 6.255059e-06, 'XCD': 0.033221, 'XDR': 0.00922, 'XOF': 7.54293, 'XPF': 1.373062,
                      'YER': 3.076698, 'ZAR': 0.236399, 'ZMK': 110.647328, 'ZMW': 0.246035, 'ZWL': 3.958182}}


def test_get_desired_currency(get_rates_dict_for_test):
    assert src.utils.get_desired_currency(get_rates_dict_for_test, 'USD') == 0.012293
    assert src.utils.get_desired_currency(get_rates_dict_for_test, 'AAA') == 'Нет информации о курсе данной валюты'


def test_check_in_file():
    path_to_file = 'tests/test_rate_data.json'

    assert src.utils.check_in_file('USD', 0.012293, get_rates_dict_for_test, path_to_file) == 'Курс не изменился и ' \
                                                                                              'составляет 0.012293 USD'