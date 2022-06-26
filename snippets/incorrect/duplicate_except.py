"""All "except" blocks should be able to catch exceptions"""

try:
    raise ValueError("raised value error")
except ValueError as e:
    print(e)
except ValueError:
    print("error")
