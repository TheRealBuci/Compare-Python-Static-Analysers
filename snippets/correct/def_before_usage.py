"""Variables, classes and functions should be defined before being used"""

class MyUnicClass:
    def __init__(self, mystring):
        self.name = mystring

    def myunicfunc(self):
        print("my func in "+self.name)

MyUnicVar = "unic var"

unic = MyUnicClass(MyUnicVar)
unic.myunicfunc()
