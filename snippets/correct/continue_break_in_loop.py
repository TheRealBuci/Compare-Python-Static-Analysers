""" "break" and "continue" should not be used outside a loop"""

import sys

def myfunc(var):
    if isinstance(var, str):
        sys.exit()
