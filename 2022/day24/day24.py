from collections import deque
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))


def lcm(x, y):
    # https://www.programiz.com/python-programming/examples/lcm
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


R = len(grid)
C = len(grid[0])

repeat = lcm(R, C)  # cycle repeats after this time
blizzards = [set() for _ in range(repeat)]
d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

for x in range(R):
    for y in range(C):
        if grid[x][y] == '^':
            dr, dc = d[1]
        elif grid[x][y] == 'v':
            dr, dc = d[2]
        elif grid[x][y] == '<':
            dr, dc = d[3]
        elif grid[x][y] == '>':
            dr, dc = d[4]
        else:
            continue

        r, c = x, y
        for i in range(0, repeat):
            blizzards[i].add((r, c))
            r, c = r + dr, c + dc
            if r == 0:
                r = R - 2
            if r == R - 1:
                r = 1
            if c == 0:
                c = C - 2
            if c == C - 1:
                c = 1

start = (0, 1)
goal = (R-1, C-2)

queue = deque()
queue.appendleft((start, 0))
visited = set()


def solve(queue, goal):
    while queue:
        pos, t = queue.pop()

        if (pos, t) in visited:
            continue

        if pos == goal:
            return t

        visited.add((pos, t))
        for r, c in [(pos[0] + dr, pos[1] + dc) for dr, dc in d]:
            if 0 <= r < R and 0 <= c < C and grid[r][c] != '#' and (r, c) not in blizzards[(t+1) % repeat]:
                queue.appendleft(((r, c), t + 1))


part1 = solve(queue, goal)
print(part1)

# back to start
queue.clear()
queue.appendleft((goal, part1))
t = solve(queue, start)

# back to goal
queue.clear()
queue.appendleft((start, t))
part2 = solve(queue, goal)
print(part2)
