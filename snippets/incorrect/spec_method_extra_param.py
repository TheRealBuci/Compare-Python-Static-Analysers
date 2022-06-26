"""Special methods should have an expected number of parameters"""

class CustomNum:
    def __init__(self, num):
        self.num = num

    def __mul__(self, second, unex):
        return self.num * second

clist = CustomNum(2)
print(clist * 5)
