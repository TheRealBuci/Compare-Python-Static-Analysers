"""Special methods should have an expected number of parameters"""

class CustomNum:
    def __init__(self, num):
        self.num = num

    def __add__(self):
        return self.num

clist = CustomNum(6)
print(clist + 3)
