# reports.py - simple reports
from data import load_expenses
from expense import CATEGORIES


def total_report():
    expenses = load_expenses()
    total = 0
    for e in expenses:
        total = total + e["amount"]
    print("Total expenses:", len(expenses))
    print("Total amount  : Rs", total)
    if len(expenses) > 0:
        print("Average       : Rs %.2f" % (total / len(expenses)))


def category_report():
    expenses = load_expenses()
    print("\nCategory-wise report")
    print("-" * 30)
    for c in CATEGORIES:
        total = 0
        for e in expenses:
            if e["category"] == c:
                total = total + e["amount"]
        print("%-12s Rs %.2f" % (c, total))


def highest_expense():
    expenses = load_expenses()
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    top = expenses[0]
    for e in expenses:
        if e["amount"] > top["amount"]:
            top = e
    print("Highest expense: Rs", top["amount"], "on", top["date"], "(" + top["category"] + ") -", top["note"])


def export_summary():
    # saves a readable report in summary.txt
    expenses = load_expenses()
    total = 0
    f = open("summary.txt", "w")
    f.write("EXPENSE SUMMARY\n")
    f.write("=" * 40 + "\n")
    for e in expenses:
        f.write(e["date"] + "  " + e["category"] + "  Rs " + str(e["amount"]) + "  " + e["note"] + "\n")
        total = total + e["amount"]
    f.write("=" * 40 + "\n")
    f.write("TOTAL: Rs " + str(total) + "\n")
    f.close()
    print("Summary saved in summary.txt")
