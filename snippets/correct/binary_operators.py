"""Identical expressions should not be used on both sides of a binary operator"""

val1 = 294
val2 = 294
val3 = "294"

if val1 == val2:
    print("Equals!")

if val2 != val3:
    print("Different!")

if val1 == val2 and val2 != val3:
    print("Both are true!")

if val1 == val2 or val2 != val3:
    print("At least one of them is true!")
