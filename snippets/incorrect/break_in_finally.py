"""Break, continue and return statements should not occur in "finally" blocks"""

for i in range(3):
    try:
        raise TypeError("type error raised")
    except TypeError as e:
        print(e)
    finally:
        print("In finally block")
        break
