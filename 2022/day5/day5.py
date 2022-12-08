import sys
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        data.append(line)


stacks1 = defaultdict(deque)
stacks2 = defaultdict(deque)
for idx in range(len(data)):
    line = data[idx]
    if line == " 1   2   3   4   5   6   7   8   9 \n":
        data = data[idx + 2:]
        break
    elements = [line[i:i+4].strip().replace("[", "").replace("]", "")
                for i in range(0, len(line), 4)]

    for i in range(9):
        if elements[i]:
            stacks1[i+1].append(elements[i])
            stacks2[i+1].append(elements[i])

for instruction in data:
    _, num, _, fr, _, to = instruction.split()
    num, fr, to = map(int, [num, fr, to])

    for _ in range(num):
        stacks1[to].appendleft(stacks1[fr].popleft())

part1 = "".join([stacks1[i + 1][0] for i in range(9)])

for instruction in data:
    _, num, _, fr, _, to = instruction.split()
    num, fr, to = map(int, [num, fr, to])

    elements = deque()
    for _ in range(num):
        elements.appendleft(stacks2[fr].popleft())
    for ele in elements:
        stacks2[to].appendleft(ele)

part2 = "".join([stacks2[i + 1][0] for i in range(9)])

print(part1)
print(part2)
