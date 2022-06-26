"""Regular expressions should be syntactically valid"""

import re

print(re.match(r"\.\.\,\.\.", "..,..,..,..,.."))
