"""Return values from functions without side effects should not be ignored"""

from datetime import date

date.today()
