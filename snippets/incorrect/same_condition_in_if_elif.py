"""Related "if/else if" statements should not have the same condition"""

num = 12
if num == 100:
    print("equals")
elif num < 100:
    print("smaller")
elif num == 100:
    print("equals again")
