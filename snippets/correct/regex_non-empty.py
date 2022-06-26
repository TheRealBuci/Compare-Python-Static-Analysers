"""Repeated patterns in regular expressions should not match the empty string"""

import re

print(re.match(r"v*", "v"))
