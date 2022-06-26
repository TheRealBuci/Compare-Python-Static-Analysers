"""Boolean expressions of exceptions should not be used in "except" statements"""

try:
    raise SyntaxError()
except (ValueError, SyntaxError, TypeError):
    print("Multiple exception catched.")
