"""The "open" builtin function should be called with a valid mode"""

with open("output.txt", "wt", encoding="utf-8") as f:
    f.write("Once again it's overwritten!")
