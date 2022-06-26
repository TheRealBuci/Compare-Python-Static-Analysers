"""Calls should not be made to non-callable values"""

class SquareClass:
    def __call__(self, number):
        number = number * number

square = SquareClass()
print(square(8))
