""""break" and "continue" should not be used outside a loop"""

val = "10"
if val < 100:
    print(val + 10)
else:
    print(val - 10)
    break
