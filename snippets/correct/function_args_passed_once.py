"""Function arguments should be passed only once"""

def my_func(a, b, c=2):
    return a * b - c

print(my_func(b=3, a=8))
