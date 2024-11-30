import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    num_elves = int(f.read().strip())

def solve1():
    prev = ([(i-1) % num_elves for i in range(0, num_elves)])
    nxt = ([(i+1) % num_elves for i in range(0, num_elves)])
    curr = 0
    left = len(prev)
    
    while left > 1:
        target = nxt[curr]
        nxt[prev[target]] = nxt[target]
        prev[nxt[target]] = prev[target]

        curr = nxt[curr]
        left -= 1

    return curr + 1

def solve2():
    i = 1
    while i * 3 < num_elves:
        i *= 3
    return num_elves - i

part1 = solve1()
part2 = solve2()

print("Part 1:", part1)
print("Part 2:", part2)
