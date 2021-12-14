import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

dirs = {'L': (0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)

def solve(numpad, pos):
    for line in data:
        for x in line:
            a,b = dirs[x]
            new_pos = (pos[0] + a, pos[1] + b)
            if numpad[new_pos[0]][new_pos[1]]:
                pos = new_pos
        print(numpad[pos[0]][pos[1]], end="")
    print()

numpad = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
pos = (2,2)
solve(numpad, pos)

numpad = [[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,2,3,4,0,0],[0,5,6,7,8,9,0],[0,0,'A','B','C',0,0],[0,0,0,'D',0,0,0],[0,0,0,0,0,0,0]]
pos = (3,1)
solve(numpad, pos)
