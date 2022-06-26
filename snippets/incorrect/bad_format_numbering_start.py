"""String formatting should not lead to runtime errors"""
print(f"""This string is manually formatted by '.format',
but starts numbering from 1.{1} """.format("first"))
