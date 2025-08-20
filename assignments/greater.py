"""
This program asks the user to enter two numbers.
It then compares the numbers and prints out
which one is greater.
If both numbers are equal, it tells the user.
"""

# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")
