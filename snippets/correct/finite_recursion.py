"""Recursion should not be infinite"""

def myrecursion(num):
    if num < 100:
        num = myrecursion(num + 5)
    return num
