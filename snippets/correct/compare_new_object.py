"""New objects should not be created only to check their identity"""

def compare(cmp):
    print(cmp == [6, 3, 8])
    print(cmp != [4, 1, 9])

compare([6, 3, 8])
