"""The number and name of arguments passed to a function should match its parameters"""

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def getname(self):
        return self.name

if __name__ == "__main__":
    dog = Dog("Berry", 5, "King Charles Spaniel")
    dog.getname("Berry")
