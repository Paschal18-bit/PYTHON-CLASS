"""
This program is a simple 'Guess the Number' game.
- The secret number is set (example: 7).
- The user is asked to guess the number.
- The program keeps asking until the user guesses correctly.
- When guessed right, it prints "Correct! You win."
"""

secret_number = 10

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You win. ")
        break
    else:
        print("Wrong guess, try again!")
