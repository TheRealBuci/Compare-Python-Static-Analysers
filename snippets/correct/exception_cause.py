"""Exceptions' "__cause__" should be either an Exception or None"""

try:
    raise ValueError("raise")
except ValueError:
    raise TypeError from None

try:
    raise ValueError("raise")
except ValueError as e:
    raise TypeError from e
