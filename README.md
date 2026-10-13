# Budget Tracker

A simple command-line budget tracker written in Python. Record your income and expenses, check your balance, and keep your data saved between sessions.

## Features

- Add income and expenses with a note
- View total income, total expenses, and current balance
- List all transactions
- Data saved automatically to a local JSON file
- Reset all data with a confirmation step
- Works on Windows, Linux, and macOS

## Requirements

- Python 3.6 or newer (no external libraries needed)

## How to run

```bash
python budget.py
```

## Project structure

```
budget-tracker/
├── budget.py     # the program
├── data.json     # created automatically on first save (ignored by Git)
└── README.md
```

## What I practiced

- Functions and the `while` loop
- Error handling with `try` / `except`
- Reading and writing JSON files
- Working with lists and dictionaries

## Ideas for the future

- Add a date to each transaction
- Delete a single transaction
- Filter transactions by type
