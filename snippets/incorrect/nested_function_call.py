"""Nested functions should not be called outside where they were defined"""

def outer():
    print("The outer function.")
    animal = "DOG"

    def inner():
        print("The inner function.")
        print("I got a ${animal}")

    inner()
    print(animal)

outer()
inner()
