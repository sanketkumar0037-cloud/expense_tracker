# data.py - reads and writes expenses from a plain text file (no JSON)
# File format (one expense per line):  id|date|category|amount|note

FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []
    try:
        f = open(FILE_NAME, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            expense = {
                "id": int(parts[0]),
                "date": parts[1],
                "category": parts[2],
                "amount": float(parts[3]),
                "note": parts[4],
            }
            expenses.append(expense)
        f.close()
    except FileNotFoundError:
        pass  # first run, file does not exist yet
    return expenses


def save_expenses(expenses):
    f = open(FILE_NAME, "w")
    for e in expenses:
        line = str(e["id"]) + "|" + e["date"] + "|" + e["category"] + "|" + str(e["amount"]) + "|" + e["note"]
        f.write(line + "\n")
    f.close()


def next_id(expenses):
    if len(expenses) == 0:
        return 1
    biggest = 0
    for e in expenses:
        if e["id"] > biggest:
            biggest = e["id"]
    return biggest + 1
