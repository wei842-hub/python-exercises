"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight sample monthly marketing budgets in euros.
# 2. Process: Read one budget, sort the list, and calculate the total.
# 3. Out: The full list, the first budget, the sorted list, and the total.
# 4. What my list is about, and what I computed from it:
# My list contains sample marketing budgets from January to August.
# The total helps me understand spending across these eight months.

budgets = [1200, 1500, 1000, 1800, 1400, 2000, 1600, 1300]

print("Monthly budgets:", budgets)
print("January budget:", budgets[0])
print("Sorted budgets:", sorted(budgets))
print("Total budget:", sum(budgets))

# Check the first three budgets against a manual calculation.
print("Total of first three budgets:", sum(budgets[:3]))
# Manual check: 1200 + 1500 + 1000 = 3700.
# The program returned 3700 for the first three items, as expected.