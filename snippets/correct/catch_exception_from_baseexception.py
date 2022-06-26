"""Caught Exceptions must derive from BaseException"""

class NewException(Exception):
    """Random custom exception derived from base exception."""

try:
    raise NewException
except NewException as e:
    print(e)
