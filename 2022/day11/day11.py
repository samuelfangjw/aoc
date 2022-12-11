from math import prod
import sys
from collections import Counter, defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        data.append(line.strip())

monkeys = []
items1 = {}
items2 = {}
inspect1 = defaultdict(int)
inspect2 = defaultdict(int)
mod = 1

for i in range(0, len(data), 7):
    monkey = int(data[i][-2])
    initial_items = list(map(int, data[i+1].replace(",", "").split()[2:]))
    op = data[i+2].replace("Operation: new = ", "")
    test = int(data[i+3].split()[-1])
    t = int(data[i+4].split()[-1])
    f = int(data[i+5].split()[-1])
    monkeys.append([monkey, op, test, t, f])
    items1[monkey] = initial_items[:]
    items2[monkey] = initial_items[:]
    mod *= test


def perform_op(old, op):
    new = eval(op)
    return new


# Part 1
for _ in range(20):
    for monkey, op, test, t, f in monkeys:
        curr = items1[monkey]

        for item in curr:
            inspect1[monkey] += 1
            worry = perform_op(item, op) // 3
            if worry % test == 0:
                items1[t].append(worry)
            else:
                items1[f].append(worry)

        items1[monkey] = []

part1 = prod([b for _, b in Counter(inspect1).most_common(2)])
print(part1)

# Part 2
for _ in range(10000):
    for monkey, op, test, t, f in monkeys:
        curr = items2[monkey]

        for item in curr:
            inspect2[monkey] += 1
            worry = perform_op(item, op) % mod
            if worry % test == 0:
                items2[t].append(worry)
            else:
                items2[f].append(worry)

        items2[monkey] = []

part2 = prod([b for _, b in Counter(inspect2).most_common(2)])
print(part2)
