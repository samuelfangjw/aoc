import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split()
        line = [line[2], line[4], line[6], line[8], line[10]]
        line = [x.replace(",", "") for x in line]
        line = [int(x) for x in line]
        input.append(line)

def score(x):
    scores = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            scores[i] += (input[j][i] * x[j])
    scores = [x if x > 0 else 0 for x in scores]
    return scores[0] * scores[1] * scores[2] * scores[3]

def calories(x):
    sum = 0
    for i in range(4):
        sum += input[i][4] * x[i]
    return sum

part1 = 0
for i in range(101):
    for j in range(101-i):
        for k in range(101-j-i):
            l = 100-j-k-i
            c = calories([i,j,k,l])
            if c != 500:
                continue
            part1 = max(part1, score([i,j,k,l]))   

print(part1)