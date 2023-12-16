import sys
import math

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
d = {}

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().replace("=", "").replace("(", "").replace(")", "").replace(",", "")
        data.append(line.split())
    steps = list([0 if x == 'L' else 1 for x in data[0][0]])
    
    for node, left, right in data[2:]:
        d[node] = (left, right)

# Part 1
idx = 0
node = "AAA"

while node != "ZZZ":
    node = d[node][steps[idx % len(steps)]]
    idx += 1

part1 = idx

# Part 2
nodes = [node for node in d if node.endswith("A")]
cycle = [0 for _ in nodes]

for i, node in enumerate(nodes):
    idx = 0
    while not node.endswith("Z"):
        node = d[node][steps[idx % len(steps)]]
        idx += 1
    cycle[i] = idx

part2 = math.lcm(*cycle)

print(part1, part2)
