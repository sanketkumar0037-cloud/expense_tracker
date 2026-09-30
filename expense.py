# expense.py - add, view, edit and delete expenses
from data import load_expenses, save_expenses, next_id

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Education", "Other"]


def valid_date(text):
    # simple check for YYYY-MM-DD
    parts = text.split("-")
    if len(parts) != 3:
        return False
    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    return 1 <= int(parts[1]) <= 12 and 1 <= int(parts[2]) <= 31


def choose_category():
    print("Categories:")
    for i in range(len(CATEGORIES)):
        print(" ", i + 1, "-", CATEGORIES[i])
    while True:
        choice = input("Choose category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice, try again.")


def add_expense():
    expenses = load_expenses()
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if valid_date(date):
            break
        print("Wrong date format.")
    category = choose_category()
    while True:
        try:
            amount = float(input("Enter amount (Rs): "))
            if amount > 0:
                break
            print("Amount must be more than 0.")
        except ValueError:
            print("Please enter a number.")
    note = input("Note (short): ").replace("|", "-")
    expense = {"id": next_id(expenses), "date": date, "category": category,
               "amount": amount, "note": note}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added! ID =", expense["id"])


def print_table(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    print("-" * 65)
    print("%-4s %-12s %-10s %10s  %s" % ("ID", "Date", "Category", "Amount", "Note"))
    print("-" * 65)
    for e in expenses:
        print("%-4d %-12s %-10s %10.2f  %s" % (e["id"], e["date"], e["category"], e["amount"], e["note"]))
    print("-" * 65)


def view_expenses():
    print_table(load_expenses())


def delete_expense():
    expenses = load_expenses()
    print_table(expenses)
    if len(expenses) == 0:
        return
    choice = input("Enter ID to delete: ")
    if not choice.isdigit():
        print("Invalid ID.")
        return
    for e in expenses:
        if e["id"] == int(choice):
            expenses.remove(e)
            save_expenses(expenses)
            print("Expense deleted.")
            return
    print("ID not found.")


def edit_expense():
    expenses = load_expenses()
    print_table(expenses)
    if len(expenses) == 0:
        return
    choice = input("Enter ID to edit: ")
    if not choice.isdigit():
        print("Invalid ID.")
        return
    for e in expenses:
        if e["id"] == int(choice):
            try:
                new_amount = float(input("New amount: "))
                if new_amount <= 0:
                    print("Amount must be more than 0.")
                    return
            except ValueError:
                print("Please enter a number.")
                return
            e["amount"] = new_amount
            e["note"] = input("New note: ").replace("|", "-")
            save_expenses(expenses)
            print("Expense updated.")
            return
    print("ID not found.")
