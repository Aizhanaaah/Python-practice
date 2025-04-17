import csv
from datetime import datetime
import pandas as pd


def add_transaction(date, type_, category, amount, note=''):
    if type_ not in ('income', 'expense'):
        raise ValueError("'type' has to be either 'income' or 'expense'")
    

    try:
        amount=float(amount)
    except ValueError:
        raise ValueError("'amount' has to be a number")
    if amount <= 0:
        raise ValueError("'amount' has to be a positive number")
    
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("'Date' has to be in a format 'YYYY-MM-DD' ")
    
    with open('Data/transactions.csv', mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, type_, category, amount, note])
    print('the transaction is added!')


print('Enter the date:')
date = input()
print('Enter type: income or expense?')
type_ = input()
print('Enter the category:')
category = input()
print('Enter the amount:')
amount = input()
print('Write some notes, (optional)')
note = input()    
add_transaction(date, type_, category, amount, note)
