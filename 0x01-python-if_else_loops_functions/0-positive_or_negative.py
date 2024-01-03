#!/usr/bin/python3
import random
c = random.randint(-10, 10)
if c > 0:
    print(f"{c} is positive")
elif c == 0:
    print(f"{c} is zero")
else:
    print(f"{c} is negative")
