"""The number and name of arguments passed to a function should match its parameters"""

def pyramid(a, b, c):
    print("  " + c + "  ")
    print(" " + b * 3 + " ")
    print(a * 5)


pyramid("a", "b")
