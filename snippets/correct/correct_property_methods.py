"""Property getter, setter and deleter methods should have the expected number of parameters"""

class Hedgehog:
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @name.deleter
    def name(self):
        del self.name
