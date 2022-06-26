"""Collection sizes and array length comparisons should make sense"""

newList = [0, 1, 2, 3]
if len(newList) >= 0:
    print("This is indeed always true.")
elif len(newList) < 0:
    print("This is indeed always false.")
