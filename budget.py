# budget.py - monthly budget saved in budget.txt
from data import load_expenses

BUDGET_FILE = "budget.txt"


def get_budget():
    try:
        f = open(BUDGET_FILE, "r")
        value = float(f.read().strip())
        f.close()
        return value
    except (FileNotFoundError, ValueError):
        return 0.0


def set_budget():
    try:
        value = float(input("Enter monthly budget (Rs): "))
    except ValueError:
        print("Please enter a number.")
        return
    f = open(BUDGET_FILE, "w")
    f.write(str(value))
    f.close()
    print("Budget saved.")


def check_budget():
    budget = get_budget()
    if budget == 0:
        print("Budget not set. Use 'Set budget' first.")
        return
    month = input("Enter month (YYYY-MM): ")
    spent = 0
    for e in load_expenses():
        if e["date"].startswith(month):
            spent = spent + e["amount"]
    print("Budget :", budget)
    print("Spent  :", spent)
    if spent > budget:
        print("WARNING: You crossed your budget by Rs", spent - budget)
    else:
        print("Good! Remaining: Rs", budget - spent)
