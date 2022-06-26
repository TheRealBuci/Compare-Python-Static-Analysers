"""Regex alternatives should not be redundant"""

import re

re.search("[a-z]|l", "l")
