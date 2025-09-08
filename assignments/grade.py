"""
Grade Calculator with While Loop

- Keeps asking the user for their score (0–100)
- Assigns a letter grade:
    A = 90–100
    B = 80–89
    C = 70–79
    D = 60–69
    F = below 60
- Provides encouraging feedback messages
- Handles invalid input (outside 0–100 or wrong data type)
- User can type 'exit' to stop the program
"""

while True:
    score_input = input("Enter your score (0-100) or type 'exit' to quit: ")

    if score_input.lower() == "exit":
        print("Goodbye! ")
        break

    try:
        score = int(score_input)

        if score < 0 or score > 100:
            print(" Invalid score. Please enter a number between 0 and 100.")
        elif score >= 90:
            print("Grade: A  Excellent job! Keep it up!")
        elif score >= 80:
            print("Grade: B  Great work! You can push for an A.")
        elif score >= 70:
            print("Grade: C  Good effort! Aim a little higher next time.")
        elif score >= 60:
            print("Grade: D  You passed, but there’s room for improvement.")
        else:
            print("Grade: F  Don’t give up! Study harder and try again.")

    except ValueError:
        print(" Invalid input. Please enter a number between 0 and 100 or 'exit'.")
