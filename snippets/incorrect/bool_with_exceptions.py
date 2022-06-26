"""Boolean expressions of exceptions should not be used in "except" statements"""

try:
    raise TypeError
except ValueError or TypeError:
    print("ValueError or TypeError")
