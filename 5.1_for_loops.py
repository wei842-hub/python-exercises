"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The eight monthly marketing budgets from exercise 4.0.
# 2. Process: Loop through the list and calculate each budget's share.
# 3. Out: Eight lines showing position, budget, and share of the total.
# 4. What I compute for each item, and why it is worth showing:
# I calculate each month's percentage of the total budget.
# This helps compare how spending is distributed across the months.

budgets = [1200, 1500, 1000, 1800, 1400, 2000, 1600, 1300]
total_budget = sum(budgets)

for position, budget in enumerate(budgets, start=1):
    share = budget / total_budget * 100
    print(f"Month {position}: EUR {budget}, {share:.2f}% of total")
# Test: The program printed exactly eight lines for eight budgets.
# The positions ran from 1 to 8, as expected.