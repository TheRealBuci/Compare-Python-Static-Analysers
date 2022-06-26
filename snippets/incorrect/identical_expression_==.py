"""Identical expressions should not be used on both sides of a binary operator"""

a = 23
if a == a:
    print("obviously")
else:
    print("never true")
