"""String formatting should not lead to runtime errors"""

print("""This string is {} formatted by '.format',
but mixes automatic and manual numbering.{1} """.format("first", "second"))
