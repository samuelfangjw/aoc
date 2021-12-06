import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

G = {}

with open(file) as f:
    for line in f:
        line = line.strip().split(" -> ")
        a = line[0].split()
        b = line[1]

        if len(a) == 1:
            G[b] = ["NONE", a[0], 0]
        elif len(a) == 2:
            G[b] = ["NOT", a[1], 0]
        else:
            G[b] = [a[1], a[0], a[2]]

    # For Part 2
    G['b'] = ["NONE", 16076, 0]

def solve(key):
    if isinstance(key, int):
        return key

    if key.isnumeric():
        return int(key)

    a,b,c = G[key]

    if a == "NONE":
        ret = solve(b)
    elif a == "NOT":
        ret = ~solve(b) & 0xffff
    elif a == "AND":
        ret = solve(b) & solve(c)
    elif a == "OR":
        ret = solve(b) | solve(c)
    elif a == "LSHIFT":
        ret = solve(b) << int(c)
    elif a == "RSHIFT":
        ret = solve(b) >> int(c)

    G[key] = ["NONE", ret, 0]
    return ret

print(solve("a"))


