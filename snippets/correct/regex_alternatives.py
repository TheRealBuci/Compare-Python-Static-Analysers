"""Regex alternatives should not be redundant"""

import re

mystring = "station"
re.match(r".*[aio].*", mystring)
