"""Exceptions should not be created without being raised"""

try:
    ValueError("Created a ValueError without raising it.")
except ValueError:
    print("Oh no.")
