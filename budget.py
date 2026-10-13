import json
import os

FILE_NAME = "data.json"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def load():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=2)


def add_transaction(kind):
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Please enter a number")
        pause()
        return
    if amount <= 0:
        print("Please enter a positive number")
        pause()
        return
    note = input("Enter a note: ")
    transactions.append({"type": kind, "amount": amount, "note": note})
    save()
    print("Saved!")
    pause()


def show_balance():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    print("Total income:  ", total_income)
    print("Total expenses:", total_expense)
    print("Balance:       ", total_income - total_expense)
    pause()


def show_transactions():
    if not transactions:
        print("No transactions yet.")
    else:
        for i, t in enumerate(transactions, start=1):
            print(f"{i}. {t['type']:8} {t['amount']:>10}  {t['note']}")
    pause()


def reset_data():
    global transactions
    confirm = input("Delete ALL transactions? (yes/no): ").strip().lower()
    if confirm == "yes":
        transactions = []
        save()
        print("All data has been reset.")
    else:
        print("Cancelled.")
    pause()


transactions = load()

while True:
    clear()
    print("1/ Add income")
    print("2/ Add expense")
    print("3/ Show balance")
    print("4/ Show transactions")
    print("5/ Reset all data")
    print("6/ Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number")
        pause()
        continue

    if choice == 1:
        add_transaction("income")
    elif choice == 2:
        add_transaction("expense")
    elif choice == 3:
        show_balance()
    elif choice == 4:
        show_transactions()
    elif choice == 5:
        reset_data()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice, choose from 1 to 6")
        pause()
