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
df = pd.read_csv('transactions.csv')

total_income = df[df['Type'] == 'income']['Amount'].sum()
total_expense = df[df['Type'] == 'expense']['Amount'].sum()

print(f"Total income: {total_income}")
print(f"Total expense: {total_expense}")

category_report = df.groupby(['Type', 'Category'])['Amount'].sum()
print("\n📊 Report by Category:")
print(category_report)


top_expenses = df[df['Type'] == 'expense'].sort_values(by='Amount', ascending=False).head(5)
print("\n💸 Top Expenses:")
print(top_expenses[['Date', 'Category', 'Amount', 'Comment']])

current_month = datetime.now().month
current_year = datetime.now().year

df_filtered_income = df[
    (pd.to_datetime(df['Date']).dt.month == current_month) &
    (pd.to_datetime(df['Date']).dt.year == current_year) &
    (df['Type'] == 'income')
]

df_filtered_expense = df[
    (pd.to_datetime(df['Date']).dt.month == current_month) &
    (pd.to_datetime(df['Date']).dt.year == current_year) &
    (df['Type'] == 'expense')
]


current_month_income = df_filtered_income['Amount'].sum()
current_month_expense = df_filtered_expense['Amount'].sum()
print(f'Your worth in current month: {current_month_income-current_month_expense} ')



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



mean_value_income = df[df['Type'] == 'income']['Amount'].sum()/len(df[df['Type'] == 'income'])

print(f'your average income: {mean_value_income}')

exceeded_expense = 10000
if exceeded_expense <=  df[df['Type'] == 'expense']['Amount'].sum():
    print('Your spending limit is too high, please cut your expenses!!!')

show_recent_data() 

