import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = int(f.read().strip())

goal = (31,39)
queue = deque([(1,1,0)])
seen = set()
part2 = None

def is_wall(x,y):
    v = x*x + 3*x + 2*x*y + y + y*y + data
    return bin(v).count('1') % 2 == 1

while queue:
    x,y,steps = queue.popleft()

    if steps == 51 and not part2:
        part2 = len(seen)
        found = True
    
    if (x,y) == goal:
        part1 = steps
        break

    if (x,y) in seen:
        continue

    if x < 0 or y < 0 or is_wall(x,y):
        continue

    seen.add((x,y))

    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        queue.append((x+dx,y+dy,steps+1))
        
print("Part 1:", part1)
print("Part 2:", part2)
