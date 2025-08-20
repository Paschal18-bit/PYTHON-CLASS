"""
This program is a simple password checker.
It asks the user to enter a password.
- If the password is "MR FRANK", it grants access.
- Otherwise, it denies access.
"""

# Ask user for password
password = input("Enter your password: ")

# Check if password is correct
if password == "MR FRANK":
    print("Access given ")
else:
    print("Access denied ")
