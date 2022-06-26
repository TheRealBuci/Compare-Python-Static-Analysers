"""Unicode Grapheme Clusters should be avoided inside regex character classes"""

import re

re.match(r"e¨|a¨", "a¨tte¨ntion")
