import pandas as pd
import csv
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import numpy as np
import random 



filename = 'transactions.csv'


if not os.path.exists(filename):
    df = pd.DataFrame(columns=["Date", "Type", "Amount", "Category"])
    df.to_csv(filename, index=False)


def generate_randome_data(rows = 100):
    CategoriesIncome = ['salary', 'freelance', 'scholarhsip', 'business', 'gift', 'rental income', 'stock divident']
    CategoriesExpense = ['grocery', 'charity', 'education', 'entertainment', 'rent', 'utilities', 'health care', 'taxes', 'transportation', 'self care']
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)
    all_data = []
    for i in range(rows):
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

        type_ = random.choice(['income', 'expense'])
        amount = round(random.uniform(1, 1000000), 2)

        if type_ == 'income':
            category = random.choice(CategoriesIncome)
        elif type_ == 'expense':
            category = random.choice(CategoriesExpense)

        all_data.append([date, type_, amount, category])

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(all_data)
        print('transactions are added!') 
        

'''
def add_transactions():
    date = datetime.now().strftime('%Y-%m-%d')
    t_type = input("Income or Expense? ").lower()
    if t_type not in ('income', 'expense'):
        raise ValueError("'type' has to be either 'income' or 'expense'")
    if t_type == 'income':
        amount = float(input('What is your income?'))
        category = input('What is the source? ')
    elif t_type == 'expense':
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
'''
generate_randome_data()

df = pd.read_csv('transactions.csv')


def show_category_report():
    category_report = df.groupby(['Type', 'Category'])['Amount'].sum()
    print("\n📊 Report by Category:")
    print(category_report)


def show_top_expenses():
    top_expenses = df[df['Type'] == 'expense'].sort_values(by='Amount', ascending=False).head(5)
    print("\n💸 Top Expenses:")
    print(top_expenses[['Date', 'Category', 'Amount', 'Comment']])


def show_recent_data():
    today = pd.to_datetime(datetime.now())
    last_week_data = today - pd.Timedelta(days=7)
    last_month_data = today - pd.Timedelta(days=30)
    df['Date'] = pd.to_datetime(df['Date']) 
    df_last_week = df[df['Date'] >= last_week_data]
    df_last_month = df[df['Date'] >= last_month_data]
    week_income = df_last_week[df_last_week['Type'] == 'income']['Amount'].sum()
    week_expense = df_last_week[df_last_week['Type'] == 'expense']['Amount'].sum()
    month_income = df_last_month[df_last_month['Type'] == 'income']['Amount'].sum()
    month_expense = df_last_month[df_last_month['Type'] == 'expense']['Amount'].sum()
    print(f"📅 Last 7 days:\n   Income: {week_income} | Expense: {week_expense}")
    print(f"📅 Last 30 days:\n   Income: {month_income} | Expense: {month_expense}")


def show_means():
    mean_value_income = df[df['Type'] == 'income']['Amount'].sum()/len(df[df['Type'] == 'income'])
    print(f'your average income: {mean_value_income}')
    mean_value_expense = df[df['Type'] == 'expense']['Amount'].sum()/len(df[df['Type'] == 'expense'])
    print(f'your average expense: {mean_value_expense}')



exceeded_expense = 10000
if exceeded_expense <=  df[df['Type'] == 'expense']['Amount'].sum():
    print('Your spending limit is too high, please cut your expenses!!!')

show_recent_data() 

