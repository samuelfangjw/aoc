import hashlib
import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

md5 = lambda x : hashlib.md5(x.encode()).hexdigest()

goal = (3,3)
start = (0,0)
queue = deque([(start, "")])

open_door = "bcdef"
paths = []

def solve():
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            paths.append(path)
            continue

        h = md5(data + path)
        if y > 0 and h[0] in open_door:
            queue.append(((x, y-1), path + "U"))
        if y < 3 and h[1] in open_door:
            queue.append(((x, y+1), path + "D"))
        if x > 0 and h[2] in open_door:
            queue.append(((x-1, y), path + "L"))
        if x < 3 and h[3] in open_door:
            queue.append(((x+1, y), path + "R"))

part1 = solve()
print("Part 1:", paths[0])
print("Part 2:", len(paths[-1]))
