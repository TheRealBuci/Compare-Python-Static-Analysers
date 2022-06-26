"""Identical expressions should not be used on both sides of a binary operator"""

a = 12
b = 13

if a == b and a == b:
    print("obviously")
else:
    print("never")
