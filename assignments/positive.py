"""
This program keeps collecting integer input from the user.
- If the number is positive (or zero), it continues asking.
- If the user enters a negative number, the program stops.
"""

while True:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative number detected. Program stopped.")
        break
    else:
        print(f"You entered: {number} (positive)")
