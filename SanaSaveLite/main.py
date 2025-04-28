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
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
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

            writer.writerow([date, type_, amount, category])
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


def load_data():
    try:
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please generate data first (Option 1).")
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category"])
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category"])


def show_category_report(df):
    if df.empty:
        print("No data available to generate report.")
        return
    
    category_report = df.groupby(['Type', 'Category'])['Amount'].sum()
    print("\n📊 Report by Category:")
    print(category_report)


def show_top_expenses(df):
    if df.empty:
        print("No data available to show top expenses.")
        return
    expenses_df = df[df['Type'] == 'expense']
    top_expenses = expenses_df.sort_values(by='Amount', ascending=False).head(5)
    print("\n💸 Top Expenses:")
    print(top_expenses[['Date', 'Category', 'Amount']])


def show_recent_data(df):
    today = pd.to_datetime(datetime.now().date())
    last_week_data = today - pd.Timedelta(days=7)
    last_month_data = today - pd.Timedelta(days=30)
    df_last_week = df[df['Date'] >= last_week_data]
    df_last_month = df[df['Date'] >= last_month_data]
    week_income = df_last_week[df_last_week['Type'] == 'income']['Amount'].sum()
    week_expense = df_last_week[df_last_week['Type'] == 'expense']['Amount'].sum()
    month_income = df_last_month[df_last_month['Type'] == 'income']['Amount'].sum()
    month_expense = df_last_month[df_last_month['Type'] == 'expense']['Amount'].sum()
    print(f"📅 Last 7 days:\n   Income: {week_income} | Expense: {week_expense}")
    print(f"📅 Last 30 days:\n   Income: {month_income} | Expense: {month_expense}")


def show_means(df):
    if df.empty:
        print("No data available to calculate means.")
        return
    mean_value_income = df[df['Type'] == 'income']['Amount'].mean() 
    print(f'your average income: {mean_value_income}')
    mean_value_expense = df[df['Type'] == 'expense']['Amount'].mean()
    print(f'your average expense: {mean_value_expense}')


def check_expense_limit(df, limit=10000):
    current_month = datetime.now().month
    current_month_expenses_sum = df[
        (df['Type'] == 'expense') &
        (df['Date'].dt.month == current_month)]['Amount'].sum()
    if current_month_expenses_sum >= limit:
        print('Warning: Your spending for this month is too high!')


generate_randome_data(rows = 100)
df = load_data()
show_category_report(df)
show_top_expenses(df)
show_recent_data(df)
show_means(df)
check_expense_limit(df, limit=10000)
