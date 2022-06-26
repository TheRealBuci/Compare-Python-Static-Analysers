"""Only defined names should be listed in "__all__" """

mynum = 19
mystring = "nineteen"

def myfunc():
    pass

__all__ = [
    "mynum",
    "mystring",
    "myfunc"
]
