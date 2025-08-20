"""
This program is a simple game called Odd or Even.
The program asks the user to enter a number.
It then checks if the number is odd or even
and prints the result.
"""

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print(f"The number {number} is EVEN.")
else:
    print(f"The number {number} is ODD.")
