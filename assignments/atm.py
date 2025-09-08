"""
ATM Simulator Console App
- Starts with a balance of $1000
- Shows a simple ATM menu:
    1. Check Balance
    2. Deposit
    3. Withdraw
- Updates balance after transactions
"""

balance = 1000  # starting balance

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: ${balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"Transaction successful! New balance: ${balance}")
        else:
            print(" Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print(" Invalid withdrawal amount.")
        elif amount > balance:
            print(" Insufficient funds. Transaction failed.")
        else:
            balance -= amount
            print(f"Transaction successful! New balance: ${balance}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye 👋")
        break

    else:
        print(" Invalid choice. Please select 1, 2, 3, or 4.")
