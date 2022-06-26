"""Regex boundaries should not be used in a way that can never be matched"""

import re

print(re.match(r"$[1-9]+^", "123"))
