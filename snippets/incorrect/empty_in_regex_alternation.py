"""Alternation in regular expressions should not contain empty alternatives"""

import re
re.match(r"alpha|beta||delta", "gamma")
