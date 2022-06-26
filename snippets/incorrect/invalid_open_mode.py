"""The "open" builtin function should be called with a valid mode"""

filename = "file.txt"

with open(filename, "aw", encoding="utf-8") as f:
    f.write("A new paragraph...")
