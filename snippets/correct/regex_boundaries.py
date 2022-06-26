"""Regex boundaries should not be used in a way that can never be matched"""

import re

print(re.match("^regex$", "regex"))
