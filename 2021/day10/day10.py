import sys
from statistics import median

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append([x for x in line])

legal =[]

# Part 1
part1 = 0
for line in data:
    stack = []
    pts = 0
    for x in line:
        if x == '(' or x == '[' or  x == '{' or x == '<':
            stack.append(x)
        else:
            y = stack.pop()
            if x == ')' and y != '(':
                pts = 3
                break
            if x == ']' and y != '[':
                pts = 57
                break
            if x == '}' and y != '{':
                pts = 1197
                break
            if x == '>' and y != '<':
                pts = 25137
                break
    if pts == 0:
        legal.append(line)
    part1 += pts

print(part1)

# Part 2
scores = []
for line in legal:
    stack = []
    for x in line:
        if x == '(' or x == '[' or  x == '{' or x == '<':
            stack.append(x)
        else:
            y = stack.pop()
    pts = 0
    while stack:
        x = stack.pop()
        pts *= 5
        if x == '(':
           pts += 1
        if x == '[':
            pts += 2
        if x == '{':
            pts += 3
        if x == '<':
            pts += 4
    scores.append(pts)
    
part2 = median(scores)
print(part2)
