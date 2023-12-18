import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()
    maps = [x.splitlines() for x in data.split('\n\n') if x]

def num_differ(x,y):
    smudges = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            smudges += 1
        if smudges > 1:
            break
    return smudges

part1, part2 = 0, 0
for m in maps:
    # Transpose matrix
    mc = []
    for i in range(len(m[0])):
        x = ""
        for j in range(len(m)):
            x += m[j][i]
        mc.append(x)

    # Rows
    for i in range(len(m)):
        x = 0
        if (len(m)-i-2) < 0:
            continue
        
        for j in range(min(i, len(m)-i-2) + 1):
            x += num_differ(m[i-j], m[i+j+1])

        if x == 0:
            part1 += (i + 1) * 100
        if x == 1:
            part2 += (i + 1) * 100

    # Columns
    for i in range(len(mc)):
        x = 0
        if (len(mc)-i-2) < 0:
            continue

        for j in range(min(i, len(mc)-i-2) + 1):
            x += num_differ(mc[i-j], mc[i+j+1])

        if x == 0:
            part1 += i + 1
        if x == 1:
            part2 += i + 1
    
print(part1, part2)
