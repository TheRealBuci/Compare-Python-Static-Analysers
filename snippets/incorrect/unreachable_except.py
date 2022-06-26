"""All "except" blocks should be able to catch exceptions"""

try:
    raise IndentationError("raised an indentation error")
except SyntaxError as e:
    print("Syntax Error " + str(e))
except IndentationError:
    print("Indentation Error never executed")
