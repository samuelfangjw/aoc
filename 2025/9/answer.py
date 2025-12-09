import heapq
import sys


file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    points = [list(map(int, line.strip().split(","))) for line in f.readlines()]

heap = []
max_area = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        width = abs(points[i][0] - points[j][0]) + 1
        height = abs(points[i][1] - points[j][1]) + 1
        area = width * height
        heap.append((-area, (i, j)))
        max_area = max(max_area, area)

heapq.heapify(heap)

x_vals = {x: idx + 1 for idx, x in enumerate(sorted({p[0] for p in points}))}
y_vals = {y: idx + 1 for idx, y in enumerate(sorted({p[1] for p in points}))}

grid = [[1 for _ in range(len(y_vals) + 2)] for _ in range(len(x_vals) + 2)]

for i in range(len(points)):
    p1, p2 = points[i], points[i - 1]
    x1, y1 = (x_vals[p1[0]], y_vals[p1[1]])
    x2, y2 = (x_vals[p2[0]], y_vals[p2[1]])

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[x][y] = 2


def dfs(gx, gy):
    stack = [(gx, gy)]
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and grid[cx][cy] == 1:
            grid[cx][cy] = 0
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))


dfs(0, 0)

max_valid_area = 0
while True:
    area, (i, j) = heapq.heappop(heap)
    area = -area

    p1, p2 = points[i], points[j]
    x1, y1 = (x_vals[p1[0]], y_vals[p1[1]])
    x2, y2 = (x_vals[p2[0]], y_vals[p2[1]])

    x_range = range(min(x1, x2), max(x1, x2) + 1)
    y_range = range(min(y1, y2), max(y1, y2) + 1)

    if all(grid[x][y] > 0 for x in x_range for y in y_range):
        max_valid_area = area
        break


print("Part 1:", max_area)
print("Part 2:", max_valid_area)
