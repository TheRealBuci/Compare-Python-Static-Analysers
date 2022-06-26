"""All branches in a conditional structure should not have exactly the same implementation"""

def func():
    pass

num = 10

if num > 10:
    func()
elif num == 10:
    func()
else:
    func()
