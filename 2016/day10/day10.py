from collections import defaultdict
from math import prod
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

vals = defaultdict(list)
instructions = {}

with open(file) as f:
    for line in f:
        line = line.strip()
        if line.startswith("value"):
            s = line.split()
            value = int(s[1])
            bot = int(s[5])
            vals[bot].append(value)
        else:
            s = line.split()
            bot = int(s[1])
            low_dest = s[5]
            low = int(s[6])
            high_dest = s[10]
            high = int(s[11])
            instructions[bot] = (low_dest, low, high_dest, high)

queue = [(bot, arr) for bot, arr in vals.items() if len(arr) == 2]
output = [0,0,0]

while queue:
    bot, arr = queue.pop()
    arr.sort()
    del vals[bot]

    low_dest, low, high_dest, high = instructions[bot]
    if low_dest == "bot":
        vals[low].append(arr[0])
        if len(vals[low]) == 2:
            queue.append((low, vals[low]))
    else:
        if low < 3:
            output[low] = arr[0]
    if high_dest == "bot":
        vals[high].append(arr[1])
        if len(vals[high]) == 2:
            queue.append((high, vals[high]))
    else:
        if high < 3:
            output[high] = arr[1]
    
    if (arr[0] == 17 and arr[1] == 61):
        part1 = bot
        print(part1)

part2 = prod(output)
print(part2)
