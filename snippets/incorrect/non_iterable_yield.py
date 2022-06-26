"""Iterable unpacking, "for-in" loops and "yield from" should use an Iterable object"""

num = 5

def gen():
    yield from num
