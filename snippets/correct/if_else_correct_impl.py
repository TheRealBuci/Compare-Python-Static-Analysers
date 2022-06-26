"""All branches in a conditional structure should not have exactly the same implementation"""

def devide(a, b):
    if b == 0:
        print(0)
    elif a > 0:
        print(a / b)
    else:
        print(a / b * (-1))

devide(8, -2)
