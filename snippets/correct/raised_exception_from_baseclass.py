"""Raised Exceptions must derive from BaseException"""

class NewException(Exception):
    """A new exception class from base exception."""

try:
    raise NewException()
except NewException as e:
    print(e)
