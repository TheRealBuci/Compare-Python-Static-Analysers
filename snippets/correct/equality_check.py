"""Silly equality checks should not be made"""

class CheckEqual:
    def __init__(self, num):
        self.num = num

    def __eq__(self, eq):
        return self.num == eq

num1 = CheckEqual(5)
num2 = 5
num3 = 6

print(num1 == num2)
print(num2 == num1)
print(num1 != num3)
