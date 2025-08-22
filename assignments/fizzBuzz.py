"""
This program prints numbers from 1 to 30 using a while loop.
- If a number is divisible by 3, it prints "fizz".
- If a number is divisible by 5, it prints "buzz".
- Otherwise, it prints the number itself.
"""

num = 1   # starting point

while num <= 30:   # loop until 30
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")   # if divisible by both 3 and 5
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    
    num += 1  # move to the next number
