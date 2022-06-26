"""Regex lookahead assertions should not be contradictory"""

import re

print(re.match(r"(?=a)b", "a"))
