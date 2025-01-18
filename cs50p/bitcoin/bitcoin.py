import sys
import requests
import json

try:
    dolar = float(sys.argv[1])
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')
else:
    bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bit_json = bitcoin.json()
    bit_value = bit_json.get('bpi').get('USD').get('rate_float')
    amount = bit_value * dolar
    print(f'${amount:,.4f}')

