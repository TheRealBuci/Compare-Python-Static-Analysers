"""Calls should not be made to non-callable values"""

class Castle:
    def __init__(self, health):
        self.health = health

castle = Castle(30)
castle()
