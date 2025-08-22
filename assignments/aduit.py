"""
This program keeps asking the user to enter their age.
- If the age is 18 or below, it keeps running.
- If the age is greater than 18, it stops and says "Access granted".
"""

while True:
    age = int(input("Enter your age: "))

    if age > 18:
        print("Access granted  (Adults only)")
        break
    else:
        print("Access denied  (You must be above 18)")
