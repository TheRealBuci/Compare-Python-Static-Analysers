"""Variables, classes and functions should be either defined or imported"""

class MyClass:
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return str(self.value)

def myfunc():
    myvar = 3
    myc = MyClass(myvar)
    print(myc)

myfunc()
