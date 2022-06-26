"""Raised Exceptions must derive from BaseException"""

class MyException:
    """Incorrect exception, not deriving from BaseException."""

raise MyException
