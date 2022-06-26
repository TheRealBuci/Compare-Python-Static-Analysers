"""Regex lookahead assertions should not be contradictory"""

import re

print(re.match(r"val(?=ue)", "value"))
