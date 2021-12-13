import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
dots = set()
folds = []

with open(file) as f:
    for line in f:
        line = line.strip().split(",")
        if len(line) == 2:
            a,b = line
            dots.add((int(b), int(a))) # Flipped to match input
        else:
            line = line[0].split()
            if line:
                a,b = line[2].split("=")
                b = int(b)
                folds.append((a,b))

def fold(t, k):
    global dots
    if t == 'y':
        dots = set((x,y) if x < k else (k-(x-k), y) for x,y in dots)
    if t == 'x':
        dots = set((x,y) if y < k else (x, k-(y-k)) for x,y in dots)

# Part 1
t, k = folds[0]
fold(t,k)
print(len(dots))
folds = folds[1:]

# Part 2
for t,k in folds:
    fold(t,k)

maxX = max(x for x,_ in dots) + 1
maxY = max(y for _,y in dots) + 1
G = [[' ' for _ in range(maxY)] for _ in range(maxX)]

for x,y in dots:
    G[x][y] = "\u2588"

for x in G:
    print("".join(x))
