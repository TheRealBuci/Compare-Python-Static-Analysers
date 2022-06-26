"""Regex alternatives should not be redundant"""

import re

re.sub(r"[e¨l¨]", "X", "e¨ve¨rywhe¨re¨")
