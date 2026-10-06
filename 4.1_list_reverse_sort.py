"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The same eight monthly marketing budgets from exercise 4.0.
# 2. Process: Display four orders without changing the original list.
# 3. Out: Original, reversed, ascending, and descending orders.
# 4. My four orders, and which ones modify the original:
# Original order: Read the list without changing it.
# Reversed order: Slicing creates a new list.
# Ascending order: sorted() creates a new list.
# Descending order: sorted(..., reverse=True) creates a new list.
# None of these changes the original.
# In contrast, list.sort() and list.reverse() modify a list in place.
# Test: The final list matches exercise 4.0 item by item.
# The equality check returned True, as expected.
budgets = [1200, 1500, 1000, 1800, 1400, 2000, 1600, 1300]
original_copy = budgets.copy()

print("Original order:", budgets)
print("Reversed order:", budgets[::-1])
print("Ascending order:", sorted(budgets))
print("Descending order:", sorted(budgets, reverse=True))

print("Original unchanged:", budgets == original_copy)
print("Original list at the end:", budgets)