"""Non-existing class members should not get called"""

class Backpack:
    def __init__(self, size, pockets):
        self.size = size
        self.pockets = pockets

bp = Backpack("Medium", 8)
print(bp.size)
print(bp.pockets)
print(bp.color)
