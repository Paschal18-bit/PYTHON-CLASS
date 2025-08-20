"""
This program demonstrates basic arithmetic operations in Python.
It creates two variables and performs:

1. Addition
2. Subtraction
3. Multiplication
4. Division

The result of each operation is displayed with an explanatory message.
"""

# Create two variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


sum = num1 + num2
difference = num1 - num2
quotient = num1 / num2
product = num1 * num2

# Ask the user which operation they want
operation = input("Choose an operation (+, -, *, /): ")

# Perform the chosen operation using if...elif...else
if operation == "+":
    result = num1 + num2
    print(f"This is the sum of the two numbers: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"This is the difference of the two numbers: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"This is the product of the two numbers: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"This is the quotient of the two numbers: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose +, -, * or /.")




