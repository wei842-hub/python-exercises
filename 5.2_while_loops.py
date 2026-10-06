"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer about whether the campaign is ready.
# 2. Process: Repeat the question until the answer is yes or three attempts are used.
# 3. Out: A summary showing the number of attempts and the final status.
# 4. My stop condition, my attempt limit, my summary:
# Stop when the user answers yes. Allow a maximum of three attempts.
# Accept capitals and extra spaces by using strip() and lower().
# At the limit, stop and report that readiness was not confirmed.
# The summary shows attempts used and whether readiness was confirmed.

attempts = 0
max_attempts = 3
confirmed = False

while attempts < max_attempts and not confirmed:
    answer = input("Is the campaign ready? Enter yes to confirm: ")
    attempts += 1

    if answer.strip().lower() == "yes":
        confirmed = True
    else:
        print("Readiness not confirmed.")

print(f"Attempts used: {attempts}")

if confirmed:
    print("Summary: Campaign readiness confirmed.")
else:
    print("Summary: Attempt limit reached. Readiness not confirmed.")