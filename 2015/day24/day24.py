import sys
import itertools
import math

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(int(line))

def part1():
    target = sum(data) // 3
    FOUND = False
    QE = math.inf
    for i in range(1, len(data)):
        if FOUND:
            break
        for x in (z for z in itertools.combinations(data, i) if sum(z) == target):
            y = list(set(data) - set(x))
            for j in range(i, len(data)):
                if (z for z in itertools.combinations(y, j) if sum(z) == target):
                    FOUND = True
                    QE = min(math.prod(x), QE)
    print(QE)

def part2():
    target = sum(data) // 4
    FOUND = False
    QE = math.inf
    for i in range(1, len(data)):
        if FOUND:
            break
        for x in (z for z in itertools.combinations(data, i) if sum(z) == target):
            x2 = list(set(data) - set(x))
            SKIP = False
            for j in range(i, len(data)):
                for y in (z for z in itertools.combinations(x2, j) if sum(z) == target):
                    y2 = list(set(x) - set(y))
                    for k in range(j, len(data)):
                        if (z for z in itertools.combinations(y2, k) if sum(z) == target):
                            FOUND = True
                            SKIP = True
                            QE = min(math.prod(x), QE)
                            break
                    if SKIP:
                        break
                if SKIP:
                    break
    print(QE)

part1()
part2()
