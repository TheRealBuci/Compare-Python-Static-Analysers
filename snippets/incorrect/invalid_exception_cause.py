"""Exceptions' "__cause__" should be either an Exception or None"""

try:
    raise TypeError("invalid exception")
except TypeError:
    raise ValueError("invalid as well") from "the cause"
