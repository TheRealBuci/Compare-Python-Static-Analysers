"""Identical expressions should not be used on both sides of a binary operator"""

a = 23
b = 25

if a != b or a != b:
    print("obvious")
else:
    print("never")
