"""Collection content should not be replaced unconditionally"""

def set_value(mlist):
    mlist[5:8] = [11, 12]
    mlist[5:8] = [11, 12]
    print(mlist)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
set_value(mylist)
