"""Function arguments should be passed only once"""

def add_and_mult(a, b, c):
    return a + b * c

add_and_mult(8, 2, 3, c=3)
