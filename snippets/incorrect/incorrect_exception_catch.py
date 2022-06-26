"""Caught Exceptions must derive from BaseException"""

class MyException:
    """An exception class not deriving from BaseException"""

try:
    one = 1
    two = "two"
    raise ValueError
except MyException:
    print("Not a correct exception")
