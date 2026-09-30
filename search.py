# search.py - search expenses
from data import load_expenses
from expense import print_table, choose_category


def search_by_category():
    category = choose_category()
    result = []
    for e in load_expenses():
        if e["category"] == category:
            result.append(e)
    print_table(result)


def search_by_month():
    month = input("Enter month (YYYY-MM): ")
    result = []
    for e in load_expenses():
        if e["date"].startswith(month):
            result.append(e)
    print_table(result)


def search_by_keyword():
    word = input("Enter keyword: ").lower()
    result = []
    for e in load_expenses():
        if word in e["note"].lower():
            result.append(e)
    print_table(result)
