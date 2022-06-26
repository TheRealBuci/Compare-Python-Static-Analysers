"""Special methods should have an expected number of parameters"""

class Numbering:
    def __init__(self, num):
        self.number = num

    def __add__(self, num):
        return self.number + num + 3

    def __mul__(self, num):
        return self.number * num * 3

numb = 8
calc = Numbering(3)

print(calc + numb)
print(calc * numb)
