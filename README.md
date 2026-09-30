# expense_tracker
Most students have trouble remembering where their pocket money went by the end of the month. I built this Expense Tracker in Python to make that easier. You can note down your daily expenses, look them up later, and see simple reports, so it's easier to spend with a bit more control.

# Expense Tracker

## Introduction
This is a simple Expense Tracker made using Python.
It is designed to help students keep a record of their daily spending. The program allows the user to add expenses, edit or delete them, search for expenses, see reports and check the monthly budget.

**Made by:** Sanket Kumar (Reg. No. 26BAI10751)

## Features
- Add expense
- View all expenses
- Edit expense
- Delete expense
- Search by category
- Search by month
- Search by keyword
- Total report (count, total and average)
- Category-wise report
- Show highest expense
- Set monthly budget
- Check budget with warning
- Save summary in a text file
- Save expenses and budget in text files

## Technologies Used
- Python
- Lists and dictionaries
- Functions
- If-else statements
- For loop
- While loop
- String handling
- Exception handling
- Modules
- File handling

## Project Files
- main.py - Main program and menu
- expense.py - Add, view, edit and delete expenses
- search.py - Search by category, month and keyword
- reports.py - Reports and summary file
- budget.py - Set and check monthly budget
- data.py - Reads and writes expense data
- expenses.txt - Stores all expenses
- budget.txt - Stores the monthly budget
- summary.txt - Created when the summary is saved
- statement.md - Problem statement

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```
python main.py
```

4. Select an option from the menu.

Only Python 3 is needed. Nothing else has to be installed.

## Main Menu
1. Add expense
2. View all expenses
3. Edit expense
4. Delete expense
5. Search by category
6. Search by month
7. Search by keyword
8. Total report
9. Category report
10. Highest expense
11. Set monthly budget
12. Check budget
13. Save summary to file
0. Exit

## Data Storage
The program uses text files to store data. No JSON or database is used.

- expenses.txt stores one expense per line in this format: `id|date|category|amount|note`
- budget.txt stores the monthly budget.
- summary.txt stores the saved summary report.

Example line in expenses.txt:

```
3|2026-09-05|Education|450.0|Notebooks and pens
```

## Testing
The following functions were tested:
- Adding an expense
- Viewing expenses
- Editing an expense
- Deleting an expense
- Search by category, month and keyword
- Total report, category report and highest expense
- Setting and checking the budget (within budget and over budget)
- Saving the summary file
- Wrong date, wrong category, negative amount and text instead of number
- Wrong ID while editing or deleting
- Running the program with no data file
- Data saving after restarting the program

To test, run `python main.py` and try the options above. For example, choose option 4 and enter ID 99. It should show "ID not found."

## Future Improvements
- Check real calendar dates (for example, reject 2026-02-31)
- Do not accept a negative budget
- Edit date and category also
- Budget for each category
- Export to CSV
- Charts for spending
- Login system
- Database storage
- Better user interface

## Conclusion
The Expense Tracker is a simple Python project that helps a student record expenses and control spending. It uses basic Python concepts learned in the first semester.
