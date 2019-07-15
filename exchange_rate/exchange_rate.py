#!/usr/bin/env python3

import json
import requests

try:
    amount = int(input('amount: '))
except ValueError:
    amount = '1'
    print('You did not enter a number so we put 1 for you')

try:
    rate_from = input('from: ').upper()
    rate_to = input('to: ').upper()
except ValueError:
    print('You did not enter a true currency so here is usd to eur')
    rate_from = 'USD'
    rate_to = 'EUR'

json_data = requests.get('https://free.currencyconverterapi.com/api/v5/convert?\
q='+str(rate_from)+'_'+str(rate_to)+'&compact=y')

exchange_rate = json.loads(json_data.text)

final_amount = exchange_rate[str(rate_from)+'_'+str(rate_to)]['val'] * amount

print(final_amount)
