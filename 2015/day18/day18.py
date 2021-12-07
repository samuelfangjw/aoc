import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
size = 100
iterations = 100

with open(file) as f:
    f = f.readlines()
    G1 = [[False for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if f[i][j] == "#":
                G1[i][j] = True
    G2 = [[x for x in y] for y in G1]

dx = [1, 0, -1]
dy = [1, 0, -1]

def neighbours(i, j, G):
    nb = [(i + x, j + y) for x in dx for y in dy if (y != 0 or x != 0)]
    nb = [x for x in nb if x[0] >= 0 and x[0] < size and x[1] >= 0 and x[1] < size]
    return sum([1 for x, y in nb if G[x][y]])


def update(G):
    NG = [[x for x in y] for y in G]
    for i in range(size):
        for j in range(size):
            N = neighbours(i,j,G)
            if NG[i][j]:
                if N != 2 and N != 3:
                    NG[i][j] = False
            else:
                if N == 3:
                    NG[i][j] = True
    return NG

# Part 1
for i in range(iterations):
    G1 = update(G1)

# Part 2
for i in range(iterations):
    G2 = update(G2)
    G2[0][0] = True
    G2[0][99] = True
    G2[99][0] = True
    G2[99][99] = True

part1 = sum(sum(row) for row in G1)
print(part1)
part2 = sum(sum(row) for row in G2)
print(part2)
