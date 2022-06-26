"""Alternation in regular expressions should not contain empty alternatives"""

import re

print(re.search(r"one|or|two", "three"))
