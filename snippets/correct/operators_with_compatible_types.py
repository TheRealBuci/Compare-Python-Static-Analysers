"""Operators should be used on compatible types"""

class SymmetricalAdd:
    def __init__(self, origin):
        self.original = origin

    def __add__(self, num):
        return self.original + num

    def __radd__(self, num):
        return num + self.original

number = SymmetricalAdd(4)
num1 = number + 5
num2 = 8 + number
