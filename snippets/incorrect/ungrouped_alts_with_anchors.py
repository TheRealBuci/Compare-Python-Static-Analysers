"""Alternatives in regular expressions should be grouped when used with anchors"""

import re

re.search("^a|b|c$", "a")
