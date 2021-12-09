import sys
from math import *

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append([int(x) for x in line])

rows = len(data)
cols = len(data[0])

def neighbours(i,j):
    dirs = [(-1,0), (0,-1), (1,0), (0,1)]
    nb = [(i + x, j + y) for x,y in dirs]
    return [x for x in nb if rows > x[0] >= 0 and cols > x[1] >= 0]

B = {}

# Part 1
def low(i, j, G):
    nb = neighbours(i,j)
    return all(G[i][j] < G[x][y] for x,y in nb)

part1 = 0

for i in range(rows):
    for j in range(cols):
        if low(i,j,data):
            B[(i,j)] = 0
            part1 += data[i][j] + 1

print(part1)

# Part 2
def basin(i,j,G):
    nb = neighbours(i,j)
    if (i,j) in V:
        return 0
    if G[i][j] == 9:
        return 0
    V.add((i,j))
    for x, y in nb:
        basin(x,y,G)

for x, y in B.keys():
    V = set()
    basin(x,y,data)
    B[(x,y)] = len(V)

part2 = prod(sorted(B.values())[-3:])

print(part2)
