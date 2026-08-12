import csv
import os

FILE_NAME = "DAY 4/expenses.csv"

# Ensure CSV file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food, Travel, etc.): ")
        amount = float(input("Enter amount: "))
        note = input("Enter note (optional): ")

        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.\n")
                return

            total = 0
            print("\n--- All Expenses ---")
            for exp in expenses:
                print(f"Date: {exp['Date']}, Category: {exp['Category']}, Amount: {exp['Amount']}, Note: {exp['Note']}")
                total += float(exp['Amount'])
            print(f"\nTotal Amount Spent: {total}\n")
    except Exception as e:
        print(f"Error reading file: {e}\n")

def category_summary():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.\n")
                return

            summary = {}
            for exp in expenses:
                category = exp['Category']
                amount = float(exp['Amount'])
                summary[category] = summary.get(category, 0) + amount

            print("\n--- Category Wise Summary ---")
            for cat, amt in summary.items():
                print(f"{cat}: {amt}")
            print()
    except Exception as e:
        print(f"Error reading file: {e}\n")

initialize_file()
while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Wise Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        category_summary()
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.\n")
