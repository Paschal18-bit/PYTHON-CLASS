"""
This program simulates a countdown timer.
It counts down from 10 to 1, with a one-second pause between numbers.
At the end, it prints "BOOM!" to simulate a detonation.
"""

import time  # to add delay

count = 10

while count > 0:
    print(count)
    time.sleep(1)  # wait for 1 second
    count -= 1

print(" BOOM! The bomb has detonated at Aptech!")
