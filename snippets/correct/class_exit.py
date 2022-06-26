""" "__exit__" should accept type, value, and traceback arguments"""

class NewClass:
    def __enter__(self):
        print("Entered the class")

    def __exit__(self, exc_type, exc_val, exc_traceb):
        print("Exited the class")
