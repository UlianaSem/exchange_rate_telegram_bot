import requests

url = "https://api.apilayer.com/exchangerates_data/latest?base=RUB&date=1995-12-13"

payload = {}
headers= {
  "apikey": "w5VosbkOtkrksSPd2QdrUQ95UxNtpjQ0"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print(result)

