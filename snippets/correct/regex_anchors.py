"""Alternatives in regular expressions should be grouped when used with anchors"""

import re

print(re.match(r"^fel$|^fal$|^fél$", "fal"))
