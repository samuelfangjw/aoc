import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
ins = []

with open(file) as f:
    for line in f:
        line = line.strip().split()
        ins.append(line)

dirs = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1)
}

mapping = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

r1,c1 = (0,0)
vertices1 = []
vertices1.append((0,0))
perimeter1 = 0

r2,c2 = (0,0)
vertices2 = []
vertices2.append((0,0))
perimeter2 = 0

for d1, n1, h in ins:
    dr1, dc1 = dirs[d1]
    dr1, dc1 = dr1*int(n1), dc1*int(n1)
    r1, c1 = r1+dr1, c1+dc1
    vertices1.append((r1,c1))
    perimeter1 += int(n1)

    n2 = int(h[2:-2], 16)
    d2 = mapping[h[-2:-1]]
    dr2, dc2 = dirs[d2]
    dr2, dc2 = dr2*n2, dc2*n2
    r2, c2 = r2+dr2, c2+dc2
    vertices2.append((r2,c2))
    perimeter2 += int(n2)

def find_area(array):
    # ref: https://arachnoid.com/area_irregular_polygon/index.html
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        ox,oy = x,y
    return a//2

part1 = find_area(vertices1) + perimeter1 // 2 + 1
part2 = find_area(vertices2) + perimeter2 // 2 + 1

print(part1, part2)
