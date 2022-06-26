"""Exceptions should not be created without being raised"""

def myfunc(string):
    try:
        if isinstance(string, str):
            print("The string: " + string)
        else:
            raise ValueError("String needed!")
    except ValueError:
        print("No worries, you can try again.")
