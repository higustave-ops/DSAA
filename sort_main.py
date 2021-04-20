"""Import modules"""
import sys

import sort_data as sd
import create_file as cf

CHOICES_LIST = ['sequence', 'size', 'priority']
ORDERS_LIST = ['asc', 'desc']

sort_choice = input("Enter sort choice<sequence,size, priority>:")

if sort_choice not in CHOICES_LIST:
    print('Invalid Sort Choice!')
    sys.exit(1)

sort_order = input("Enter sort order <asc, desc>: ")

if sort_order not in ORDERS_LIST:
    print('Invalid Sort Order!')
    sys.exit(1)

sorted_data = sd.sort_data(sort_choice, sort_order)
cf.create_file(sorted_data, sort_choice)
print('File Created Successfully!')
