import heapq
from math import prod
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    boxes = [
        (int(x), int(y), int(z))
        for line in f.readlines()
        if line.strip()
        for x, y, z in [line.strip().split(",")]
    ]


parents = list(range(len(boxes)))
sizes = [1] * len(boxes)
heap = []


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        a, b = boxes[i], boxes[j]
        d = (
            pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2)
        )  # squared distance
        heapq.heappush(heap, (d, i, j))


part1, part2 = 0, 0
pairs_to_connect = 1000 if file == "input.txt" else 10
while True:
    d, i, j = heapq.heappop(heap)
    ri, rj = find(i), find(j)

    if ri != rj:
        if sizes[ri] < sizes[rj]:
            ri, rj = rj, ri
        parents[rj] = ri
        sizes[ri] += sizes[rj]

        if sizes[ri] == len(boxes):
            a, b = boxes[i], boxes[j]
            part2 = a[0] * b[0]
            break

    pairs_to_connect -= 1
    if pairs_to_connect == 0:
        # find product of sizes of three largest components
        count = {}
        for i in range(len(boxes)):
            r = find(i)
            count[r] = sizes[r]

        part1 = prod(sorted(count.values(), reverse=True)[:3])

print("Part 1:", part1)
print("Part 2:", part2)
