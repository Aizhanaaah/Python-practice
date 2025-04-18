import pandas as pd
import csv
from datetime import datetime
import os

filename = 'transactions.csv'


if not os.path.exists(filename):
    df = pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Comment"])
    df.to_csv(filename, index=False)



def add_transactions():
    date = datetime.now().strftime('%Y-%m-%d')
    t_type = input("Income or Expense? ").lower()
    if t_type not in ('income', 'expense'):
        raise ValueError("'type' has to be either 'income' or 'expense'")
    if t_type == 'income':
        amount = float(input('What is your income?'))
        category = input('What is the source? ')
    elif t_type == 'expence':
        amount = float(input('What is your expense? ')) 
        category = input('What is the category? ')
    if amount <= 0:
        raise ValueError("'amount' has to be a positive number")
    

    comment = input('Add notes (optional)')
    



    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, amount, category, comment])
        print('transactions are added!')


add_transactions()
df = pd.read_csv('transactions.csv')
