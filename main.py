import csv
import os
from datetime import datetime

expenses = []
monthly_budgets = {} 
filename = 'expenses.csv'

# Load expenses from CSV
def load_expenses():
    if os.path.exists(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    expense = {
                        'date': row['date'],
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'description': row['description']
                    }
                    expenses.append(expense)
                except (ValueError, KeyError):
                    print("Warning: Skipping invalid entry in file.")

# Save expenses to CSV
def save_expenses():
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Expense not added.")
        return
    description = input("Enter a brief description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added.")

# View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nYour Expenses:")
    for i, e in enumerate(expenses, 1):
        if all(k in e for k in ['date', 'category', 'amount', 'description']):
            print(f"{i}. Date: {e['date']}, Category: {e['category']}, "
                  f"Amount: {e['amount']:.2f}, Description: {e['description']}")
        else:
            print(f"{i}. Incomplete entry skipped.")

# Set a budget for a specific month
def set_budget():
    month_input = input("Enter the month to set budget for (YYYY-MM): ")
    try:
        budget_amount = float(input("Enter the monthly budget: "))
        monthly_budgets[month_input] = budget_amount
        print(f"Budget of {budget_amount:.2f} set for {month_input}.")
    except ValueError:
        print("Invalid budget amount.")

# Track budget for a specific month
def track_budget():
    month_input = input("Enter the month to track budget for (YYYY-MM): ")
    budget = monthly_budgets.get(month_input)
    if budget is None:
        print("No budget set for this month.")
        return

    total = 0.0
    for e in expenses:
        try:
            expense_month = e['date'][:7]  # Extract 'YYYY-MM'
            if expense_month == month_input:
                total += e['amount']
        except:
            continue

    print(f"Total expenses for {month_input}: {total:.2f}")
    if total > budget:
        print("You have exceeded your budget!")
    else:
        print(f"You have {budget - total:.2f} left for {month_input}.")

# Main menu
def main_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Set monthly budget")
        print("4. Track monthly budget")
        print("5. Save expenses")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

load_expenses()
main_menu()
