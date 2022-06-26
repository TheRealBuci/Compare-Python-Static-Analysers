"""Loops with at most one iteration should be refactored"""

myString = "this"

while "t" in myString:
    myString = myString[:-1]
    print("In loop")
    break
