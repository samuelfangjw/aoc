from collections import deque
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

rocks = [[(0, 2), (0, 3), (0, 4), (0, 5)], [(0, 3), (1, 3), (2, 3), (1, 2), (1, 4)], [
    (0, 2), (0, 3), (0, 4), (1, 4), (2, 4)], [(0, 2), (1, 2), (2, 2), (3, 2)], [(0, 2), (0, 3), (1, 2), (1, 3)]]


def find(n):
    pastl = 20
    past = deque([-1]) * pastl
    seen = {}
    idx = -1
    maxh = 0
    offset = 0
    grid = set()

    i = 0
    while i < n:
        rock = [(x + maxh + 3, y) for x, y in rocks[i % 5]]

        while True:
            idx += 1
            if data[idx % len(data)] == '<':
                rocky = [(x, y - 1) for x, y in rock]
            else:
                rocky = [(x, y + 1) for x, y in rock]

            if all([0 <= y < 7 and (x, y) not in grid for x, y in rocky]):
                rock = rocky

            rockx = [(x-1, y) for x, y in rock]
            if all([0 <= x and (x, y) not in grid for x, y in rockx]):
                rock = rockx
            else:
                break

        grid.update(rock)
        maxh = max(max([x + 1 for x,  _ in rock]), maxh)
        past.append(rock[0][1])
        past.popleft()

        if i % len(data) > pastl:
            strpast = str(past)
            if strpast in seen:
                (j, h) = seen[strpast]
                gap = i - j
                m = (n - i) // gap
                n -= gap * m
                offset += (maxh - h) * m
            else:
                seen[strpast] = (i, maxh)

        i += 1

    return maxh + offset


part1 = find(2022)
print(part1)

part2 = find(1000000000000)
print(part2)
