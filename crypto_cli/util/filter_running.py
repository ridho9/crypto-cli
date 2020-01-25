from sys import stdin

for c in stdin.read():
    if c.isalpha():
        c = c.lower()
        print(c, end="")
