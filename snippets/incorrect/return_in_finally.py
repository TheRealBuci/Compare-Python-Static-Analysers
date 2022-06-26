"""Break, continue and return statements should not occur in "finally" blocks"""

def incorrect():
    for i in range(3):
        try:
            print(i)
            raise SyntaxError("syntax error raised")
        except SyntaxError as e:
            print(e)
        finally:
            print("In finally block")
            return
