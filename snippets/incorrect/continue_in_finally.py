"""Break, continue and return statements should not occur in "finally" blocks"""

for i in range(3):
    try:
        raise ValueError("value error raised")
    except ValueError as e:
        print(e)
    finally:
        print("In finally block")
        continue
