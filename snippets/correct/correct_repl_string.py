"""Replacement strings should reference existing regular expression groups"""

import re

print(re.sub(r"(.*)(blue)(.*)(pink)(.*)", r"\1balck\3white\5", "I like blue and pink!"))
