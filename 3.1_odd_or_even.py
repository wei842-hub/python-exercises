"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: An integer N entered by the user.
# 2. Process: Check N, then use the remainder to identify odd and even numbers.
# 3. Out: Say whether each number from 1 to N is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
# For 0: Display a message because there are no numbers from 1 to 0.
# For a negative number: Ask the user to run again with a positive number.
# For 5000: Reject it. Limit N to 100 to keep the output manageable.

n = int(input("Enter an integer from 1 to 100: "))

if n == 0:
    print("There are no numbers to check. Please enter at least 1.")
elif n < 0:
    print("Please run again and enter a positive number.")
elif n > 100:
    print("The number is too large. Please enter 100 or less.")
else:
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
# Test with 6: Three odd and three even numbers, as expected.
# Test with 0: The no-numbers message appeared, as expected.
# Test with -4: The positive-number message appeared, as expected.
# Test with 5000: The too-large message appeared, as expected.