#!/usr/bin/env python
# coding: utf-8

import requests
import pprint
pp = pprint.PrettyPrinter(depth=4)


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'

'''
#Question-3
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

#Question-4
customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
''' 

#Question-6 using model2.bin and dv from base image
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
pp.pprint(customer)

response = requests.post(url, json=customer).json()
print(response)
