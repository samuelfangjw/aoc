from math import prod
import sys


file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


with open(file) as f:
    lines = f.read().split("\n")
    lines = [line for line in lines if line]


def solve(eqns):
    res = 0
    for idx, op in enumerate(lines[-1].split()):
        if op == "+":
            res += sum(eqns[idx])
        elif op == "*":
            res += prod(eqns[idx])
    return res


def part_one():
    eqns = [[] for _ in lines[0].split()]
    for idx in range(len(lines) - 1):
        line = lines[idx]
        xs = line.split()
        for i, x in enumerate(xs):
            eqns[i].append(int(x))

    return solve(eqns)


def part_two():
    idx = 0
    eqns = [[]]
    for idx in range(len(lines[0])):
        s = ""
        for jdx in range(len(lines) - 1):
            s += lines[jdx][idx].strip()
        if s:
            eqns[-1].append(int(s))
        else:
            eqns.append([])

    return solve(eqns)


print("Part 1:", part_one())
print("Part 2:", part_two())
