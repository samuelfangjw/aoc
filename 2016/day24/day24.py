import heapq
import sys
import itertools
from copy import copy
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

grid = set()
pois = {}

for idx, line in enumerate(data):
    for jdx, char in enumerate(line):
        if char != "#" :
            grid.add((idx, jdx))
        if char != "#" and char != ".":
            if char == "0":
                start = (idx, jdx)
            pois[int(char)] = (idx, jdx)

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        pos, dist = queue.popleft()

        if pos in visited:
            continue

        visited.add(pos)

        if pos == end:
            return dist

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)

            if new_pos in grid:
                queue.append((new_pos, dist + 1))
    

distances = defaultdict(dict)
pois_found = [False for _ in range(len(pois))]
pois_found[0] = True

for poiA, poiB in itertools.combinations(pois.keys(), 2):
    dist = bfs(pois[poiA], pois[poiB])
    distances[poiA][poiB] = dist
    distances[poiB][poiA] = dist

queue = []
heapq.heappush(queue, (0, 0, pois_found))

shortest_path_to_poi = [0 for _ in range(len(pois))]
shortest_path_to_poi[0] = 1 # dummy value

while queue:
    dist, poi, pois_found = heapq.heappop(queue)

    if all(pois_found):
        if shortest_path_to_poi[poi] == 0:
            shortest_path_to_poi[poi] = dist
        if all(shortest_path_to_poi):
            break
        continue

    for new_poi in [new_poi for new_poi, found in enumerate(pois_found) if not found]:
        new_pois_found = copy(pois_found)
        new_pois_found[new_poi] = True
        new_dist = dist + distances[poi][new_poi]
        heapq.heappush(queue, (new_dist, new_poi, new_pois_found))

part1 = min(shortest_path_to_poi[1:])
part2 = min([d + distances[idx+1][0] for idx, d in enumerate(shortest_path_to_poi[1:])])

print("Part 1:", part1)
print("Part 2:", part2)
