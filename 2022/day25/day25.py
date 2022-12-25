import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()


def tonum(str):
    n = 0
    curr = 1
    for c in str[::-1]:
        if c == '=':
            n -= curr * 2
        elif c == '-':
            n -= curr
        else:
            c = int(c)
            n += curr * c
        curr *= 5
    return n


total = sum([tonum(s) for s in data.splitlines()])
s = ""
carry = 0

while total > 0:
    n = total % 5 + carry
    total = total // 5
    if n <= 2:
        s = str(n) + s
        carry = 0
    else:
        if n == 3:
            s = '=' + s
        elif n == 4:
            s = '-' + s
        else:  # n == 5
            s = '0' + s
        carry = 1

if carry:
    s = '1' + s

print(s)
