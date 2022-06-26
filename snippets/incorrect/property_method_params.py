"""Property getter, setter and deleter methods should have the expected number of parameters"""

class Dog:
    @property
    def breed(self, name):
        return self.breed

    @breed.setter
    def breed(self, breed, name):
        self.breed = breed

    @breed.deleter
    def breed(self, name):
        del self.breed
