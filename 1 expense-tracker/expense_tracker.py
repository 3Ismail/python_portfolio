import csv

def add_expense(amount, category, description):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            print("\n💰 Your Expenses:")
            for row in reader:
                print(f"Amount: {row[0]} | Category: {row[1]} | Description: {row[2]}")
    except FileNotFoundError:
        print("⚠️ No expenses found yet. Add some first!")

def main():
    print("=== Expense Tracker ===")
    while True:
        print("\n1️⃣ Add Expense\n2️⃣ View Expenses\n3️⃣ Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
