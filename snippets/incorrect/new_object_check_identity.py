"""New objects should not be created only to check their identity"""

def check(param):
    return param is [1, 2, 3]
