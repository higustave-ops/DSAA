"""import modules"""
import read_data as rd


FILE_NAME = 'items.txt'

process_data = rd.load_data(FILE_NAME)

def sort_data(choice, order):
    """Function to sort data"""
    if order == 'asc':
        sorted_items = sorted(process_data, key = lambda el: el[choice])
    else:
        sorted_items = sorted(process_data, key = lambda el: el[choice], reverse = True)
    return sorted_items
