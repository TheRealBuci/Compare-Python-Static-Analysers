"""The output of functions that don't return anything should not be used"""

with open("file.txt", "w", encoding="utf-8") as f:
    val = f.write("IT IS WRITTEN")
