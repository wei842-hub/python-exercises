"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary describing a lipstick product.
# 2. Process: Read a field, update stock, remove a field, and display all fields.
# 3. Out: The product name, missing-field messages, and the remaining fields.
# 4. My object, my five fields, and why those:
# A lipstick product for an online store.
# name: Identify the product.
# brand: Identify its manufacturer.
# price: Show its selling price in euros.
# stock: Track available units.
# channel: Record where it is sold.

product = {
    "name": "Matte Lipstick",
    "brand": "Sample Beauty",
    "price": 25.0,
    "stock": 10,
    "channel": "Online store"
}

# Read a field.
print("Product name:", product["name"])

# Change a field.
product["stock"] = 15

# Remove a field.
del product["channel"]

# Test a missing field and handle the error.
try:
    print(product["color"])
except KeyError:
    print("The color field does not exist.")

# Another safe way to read a missing field.
print("Color:", product.get("color", "Not available"))

# Display every remaining field and its value.
for field, value in product.items():
    print(f"{field}: {value}")
# Test: Reading the missing "color" field raised KeyError.
# The except block handled it, and the program continued.
# get() returned "Not available" without raising an error.