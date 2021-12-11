import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append([int(x) for x in line])

def f():
    s = 0
    flashes = []
    visited = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
            if data[i][j] > 9:
                flashes.append((i,j))
    while (flashes):
        i,j = flashes.pop()
        if (i,j) in visited:
            continue
        visited.append((i,j))
        data[i][j] = 0
        s += 1
        dx = [1,-1,0]
        dy = [1,-1,0]
        nbrs = [(i + x, j + y) for x in dx for y in dy]
        nbrs = [(x,y) for x,y in nbrs if 0 <= x < len(data) and 0 <= y < len(data[0])]
        for x, y in nbrs:
            if (x,y) in visited:
                continue
            data[x][y] += 1
            if data[x][y] > 9:
                flashes.append((x,y))
    return s

saved = [x[:] for x in data]

# Part 1
part1 = sum(f() for _ in range(100))
print(part1)

# Part 2
data = saved
t = len(data) * len(data[0])
s = 0
part2 = 0
while s != t:
    part2 += 1
    s = f()
print(part2)