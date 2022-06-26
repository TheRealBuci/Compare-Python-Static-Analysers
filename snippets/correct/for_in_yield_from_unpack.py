"""Iterable unpacking, "for-in" loops and "yield from" should use an Iterable object"""

custom_list = [6, 5, 4, 3, 2, 1, 0]

def for_in(mylist):
    for i in mylist:
        print(i)

def yield_from(mylist):
    if len(mylist) >= 2:
        yield from simple_yield(mylist)

def simple_yield(mylist):
    yield mylist[0]

def unpack(mylist):
    _, b, _, _, e, _, _ = mylist
    return b + e
