"""Recursion should not be infinite"""

def recursive_func(num):
    num = num * recursive_func(num)
    return num

recursive_func(8)
