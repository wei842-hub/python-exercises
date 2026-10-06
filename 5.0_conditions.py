"""Exercise 5.0 — Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A campaign budget in euros.
# 2. Process: Check which budget range the number belongs to.
# 3. Out: A message suggesting the campaign scale.
# 4. My ranges, my boundaries, my messages:
# Below 0: Invalid budget.
# 0 <= budget < 500: Small test campaign.
# 500 <= budget < 1500: Basic campaign.
# 1500 <= budget < 3000: Expanded campaign.
# budget >= 3000: Large campaign.
# These are sample planning thresholds.
# Higher budgets allow broader campaign activity.
# Each boundary belongs to the higher range.

budget = float(input("Enter the campaign budget in euros: "))

if budget < 0:
    print("Invalid budget: Please enter zero or a positive number.")
elif budget < 500:
    print("Small test campaign.")
elif budget < 1500:
    print("Basic campaign.")
elif budget < 3000:
    print("Expanded campaign.")
else:
    print("Large campaign.")
# Boundary tests matched the intended ranges:
# -1 was invalid; 0 and 1 were small.
# 499 was small; 500 and 501 were basic.
# 1499 was basic; 1500 and 1501 were expanded.
# 2999 was expanded; 3000 and 3001 were large.