import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
bricks = []

with open(file) as f:
    for line in f:
        line = line.strip()
        a,b = line.split('~')
        bricks.append((list(map(int,a.split(','))), list(map(int,b.split(',')))))

bricks.sort(key=lambda x:x[0][2])
height_map = defaultdict(int)
top_brick = {}
supported_by = defaultdict(set)
supports = defaultdict(set)

for idx, ((x1,y1,z1),(x2,y2,z2)) in enumerate(bricks):
    dz = z2-z1+1

    max_height = max([height_map[(x,y)] for x in range(x1,x2+1) for y in range(y1,y2+1)])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if height_map[(x,y)] == max_height and max_height > 0:
                supported_by[idx].add(top_brick[(x,y)])
                supports[top_brick[(x,y)]].add(idx)
            top_brick[(x,y)] = idx
            height_map[(x,y)] = max_height + dz

def fall(idx):
    ans = 1
    for b in supports[idx]:
        if len(supported_by[b].difference(fallen)) == 0:
            fallen.add(b)
            ans += fall(b)

    return ans

part1, part2 = 0, 0
for i in range(len(bricks)):
    disintegrate = True
    fallen = set()
    for j in supports[i]:
        if len(supported_by[j]) == 1:
            disintegrate = False
            fallen.add(j)
            part2 += fall(j)
    if disintegrate:
        part1 += 1

print(part1, part2)
