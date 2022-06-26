"""Regular expressions should be syntactically valid"""

import re

re.search(r"({", "({)")
