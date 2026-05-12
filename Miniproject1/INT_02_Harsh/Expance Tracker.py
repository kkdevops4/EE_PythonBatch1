
expenses = {
    "Food": [150]
    
}

budgets = {
    "Food": 1000
}

def add_expense():
    category = input("Enter category: ").title()
    amount = int(input("Enter amount: "))

    if category not in expenses:
        expenses[category] = []

    expenses[category].append(amount)
    print("Expense added ")

def set_budget():
    category = input("Enter category: ").title()
    amount = int(input("Enter budget amount: "))

    budgets[category] = amount
    print("Budget set ")

def show_summary():
    for category, amounts in expenses.items():
        total = sum(amounts)
        print(f"\n{category} - Total Spent: {total}")

        if category in budgets and total > budgets[category]:
            print(" Warning: Over Budget!")

def show_total_expense():
    total = 0
    for amounts in expenses.values():
        total += sum(amounts)

    print("\n Total Expense:", total)

while True:
    print("\n1. Add Expense")
    print("2. Set Budget")
    print("3. Show Summary")
    print("4. Show Total Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        set_budget()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        show_total_expense()
    elif choice == "5":
        print("Goodbye ")
        break
    else:
        print("Invalid choice ")