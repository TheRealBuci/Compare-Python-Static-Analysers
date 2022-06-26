""""return" and "yield" should not be used in the same function"""

def myFunc():
    name = "Name"
    if "N" in name:
        name = name[:-1]
        yield name
    return name
