"""Identity operators should not be used with dissimilar types"""

num1 = 295
num2 = 123

if num1 is num2:
    print("it's the same!")
