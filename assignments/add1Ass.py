
"""
This program is a simple calculator.
- It takes two numbers as input and an operation (sum, difference, product, quotient).
- It performs the chosen operation and prints the result.
- The program keeps running until the user chooses not to continue.
"""

while True:
    # user inputs, num1 and num2
    num1 = int(input("Input your first number: "))
    num2 = int(input("Enter your second number: "))

    # operation input
    op = input("Enter your operation: sum \nproduct \nquotient \ndifference \n").lower()

    # sum, difference, quotient, product
    def addition():
        sum = num1 + num2
        print(f"This is the sum: {sum}")

    def diff():
        difference = num1 - num2
        print(f"This is the difference: {difference}")

    def qout():
        qoutient = num1 / num2
        print(f"This is the quotient: {qoutient}")

    def prod():
        product = num1 * num2
        print(f"This is the product: {product}")

    # conditional operation check
    if op == "sum": 
        addition()
    elif op == "difference":
        diff()
    elif op == "quotient":
        if num2 == 0:
            print("Undefined (division by zero)")
        else:
            qout()
    elif op == "product":
        prod()
    else:
        print("Invalid operator")

    # ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Program ended. Goodbye 👋")
        break

    print("---- Restarting Calculator ----\n")