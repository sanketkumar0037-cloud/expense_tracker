# main.py - Expense Tracker (run this file)
from expense import add_expense, view_expenses, edit_expense, delete_expense
from search import search_by_category, search_by_month, search_by_keyword
from reports import total_report, category_report, highest_expense, export_summary
from budget import set_budget, check_budget


def menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Edit expense")
    print("4. Delete expense")
    print("5. Search by category")
    print("6. Search by month")
    print("7. Search by keyword")
    print("8. Total report")
    print("9. Category report")
    print("10. Highest expense")
    print("11. Set monthly budget")
    print("12. Check budget")
    print("13. Save summary to file")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            search_by_month()
        elif choice == "7":
            search_by_keyword()
        elif choice == "8":
            total_report()
        elif choice == "9":
            category_report()
        elif choice == "10":
            highest_expense()
        elif choice == "11":
            set_budget()
        elif choice == "12":
            check_budget()
        elif choice == "13":
            export_summary()
        elif choice == "0":
            print("Thank you! Bye.")
            break
        else:
            print("Invalid choice, try again.")


main()
