"""Replacement strings should reference existing regular expression groups"""

import re

mystring = r"This is my string. It makes me happy."
print(re.sub(r"(.*)(string)(.*)(happy)(.*)", r"\1apple\3hungry\6", mystring))
