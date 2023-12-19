import sys
import heapq

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(list(map(int, list(line))))

dirs = {
    0: (-1,0), # up
    1: (0,-1), # left
    2: (1,0), # down
    3: (0,1) # right
}

def solve(min, max):
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (grid[0][1],0,1,1,3))
    heapq.heappush(pq, (grid[1][0],1,0,1,2))
    
    seen = set()

    while pq:
        heat_loss, r, c, h, d = heapq.heappop(pq)

        if (r,c,h,d) in seen:
            continue
        seen.add((r,c,h,d))

        if r == len(grid)-1 and c == len(grid[0])-1 and h >= min:
            return heat_loss

        possible = []
        if h >= min:
            possible.append(d-1)
            possible.append(d+1)
        if h < max:
            possible.append(d)

        for nd in map(lambda x: x % 4, possible):
            dr, dc = dirs[nd]
            nr, nc = r+dr, c+dc

            if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                nh = 1
                if d == nd:
                    nh += h

                heapq.heappush(pq, (heat_loss+grid[nr][nc],nr,nc,nh,nd))

part1, part2 = solve(1,3), solve(4,10)
print(part1, part2)
