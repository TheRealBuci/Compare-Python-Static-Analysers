"""All "except" blocks should be able to catch exceptions"""

try:
    raise IndentationError("raised an indentation error")
except IndentationError:
    print("Indentation error!")
except SyntaxError:
    print("Every other syntax error is caught here.")
