"""Repeated patterns in regular expressions should not match the empty string"""

import re

re.match(r"(|x)*", "")
