import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

def dragon(s):
    b = list(s[::-1])
    for i in range(len(b)):
        b[i] = "0" if b[i] == "1" else "1"
    return s + "0" + "".join(b)

def checksum(s):
    c = ""
    while len(c) % 2 == 0:
        c = ""
        for i in range(0, len(s), 2):
            c += "1" if s[i] == s[i+1] else "0"
        s = c
    return c

def solve(l):
    a = data
    while len(a) < l:
        a = dragon(a)

    a = a[:l]
    return checksum(a)

print("Part 1:", solve(272))
print("Part 2:", solve(35651584))
