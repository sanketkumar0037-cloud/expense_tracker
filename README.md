# expense_tracker
Most students have trouble remembering where their pocket money went by the end of the month. I built this Expense Tracker in Python to make that easier. You can note down your daily expenses, look them up later, and see simple reports, so it's easier to spend with a bit more control.

# Expense Tracker (Python)

I made this as my first-semester project. It's a small menu-driven program that runs in the console and helps you keep track of what you spend. Everything is saved in plain text files, so there's no JSON and no database involved.

## What it can do
- Add, view, edit and delete expenses
- Search your expenses by category, month or keyword
- Show reports: total spent, spending per category, and your biggest expense
- Set a monthly budget and check whether you've gone over it
- Save a summary of your spending to `summary.txt`

## What's in the folder
| File | What it does |
|------|--------------|
| `main.py` | The main menu. Run this one. |
| `expense.py` | Adding, viewing, editing and deleting expenses |
| `search.py` | Searching by category, month and keyword |
| `reports.py` | The reports, plus saving the summary file |
| `budget.py` | Setting and checking the monthly budget |
| `data.py` | Reading and writing `expenses.txt` |
| `expenses.txt` | Where your expenses are stored, one per line as `id\|date\|category\|amount\|note` |
| `budget.txt` | Where your budget is stored |
| `statement.md` | The problem statement |

## How to run it
```
python main.py
```
You only need Python 3. There's nothing else to install.

## Author
Sanket Kumar
