"""Operators should be used on compatible types"""

myNum = 15
myString = "a string"
result = myNum if myNum % 5 == 0 else myNum + myString
print(result)
