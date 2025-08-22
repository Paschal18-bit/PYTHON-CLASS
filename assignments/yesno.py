"""
This program keeps asking the user if they want to continue.
- If the user types 'yes', the program keeps running.
- If the user types 'no', the program ends.
"""

while True:
    choice = input("Do you want to continue? (yes/no): ").strip().lower()

    if choice == "yes":
        print("Okay, continuing the program... ")
    elif choice == "no":
        print("Program ended. Goodbye ")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
