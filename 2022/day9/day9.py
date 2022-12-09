import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)


knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

visited1 = set()
visited2 = set()
visited1.add((0, 0))
visited2.add((0, 0))

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


for l in data:
    dir, n = l.split()

    for _ in range(int(n)):
        hr, hc = moves[dir]
        knots[0] = (knots[0][0] + hr, knots[0][1] + hc)

        for i in range(1, 10):
            if abs(knots[i][0] - knots[i-1][0]) <= 1 and abs(knots[i][1] - knots[i-1][1]) <= 1:
                continue
            else:
                tr = cmp(knots[i-1][0], knots[i][0])
                tc = cmp(knots[i-1][1], knots[i][1])
                knots[i] = (knots[i][0] + tr, knots[i][1] + tc)
        visited1.add(knots[1])
        visited2.add(knots[9])

part1 = len(visited1)
part2 = len(visited2)
print(part1)
print(part2)
