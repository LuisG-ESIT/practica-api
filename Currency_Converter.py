import requests

class CurrencyConverter:
  def __init__(self, API_KEY):
    self.api_key = API_KEY
    self.url = f"https://v6.exchangerate-api.com/v6/30b54b403e5119b5f5e2929b/latest/"

  def get_exchange_rate(self, from_currency, to_currency):
    response = requests.get(self.url + from_currency)
    data = response.json()
    if response.status_code == 200:
      rates = data['conversion_rates']
      return rates.get(to_currency, None)
    else:
      print(f"Error: {data['error-type']}")
      return None
      
