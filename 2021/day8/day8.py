import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
input = []
output = []

with open(file) as f:
    for line in f:
        line = line.strip().split(" | ")
        input.append([''.join(sorted(a)) for a in line[0].split()])
        output.append([''.join(sorted(a)) for a in line[1].split()])

# Part 1
part1 = sum([sum([1 for x in li if len(x) == 7 or len(x) == 2 or len(x) == 3 or len(x) == 4]) for li in output])
print(part1)

# Part 2
part2 = 0
for i in range(len(input)):
    li = input[i]
    segments = [['a','b','c','d','e','f','g'] for _ in range(7)]
    len5 = [x for x in li if len(x) == 5]
    len6 = [x for x in li if len(x) == 6]

    for combi in li:
        if len(combi) == 2:
            segments[0] = [x for x in segments[0] if x in combi]
            segments[1] = [x for x in segments[1] if x in combi]
            segments[2] = [x for x in segments[2] if x not in combi]
            segments[3] = [x for x in segments[3] if x not in combi]
            segments[4] = [x for x in segments[4] if x not in combi]
            segments[5] = [x for x in segments[5] if x not in combi]
            segments[6] = [x for x in segments[6] if x not in combi]
        if len(combi) == 3:
            segments[0] = [x for x in segments[0] if x in combi]
            segments[1] = [x for x in segments[1] if x in combi]
            segments[2] = [x for x in segments[2] if x not in combi]
            segments[3] = [x for x in segments[3] if x in combi]
            segments[4] = [x for x in segments[4] if x not in combi]
            segments[5] = [x for x in segments[5] if x not in combi]
            segments[6] = [x for x in segments[6] if x not in combi]
        if len(combi) == 4:
            segments[0] = [x for x in segments[0] if x in combi]
            segments[1] = [x for x in segments[1] if x in combi]
            segments[2] = [x for x in segments[2] if x not in combi]
            segments[3] = [x for x in segments[3] if x not in combi]
            segments[4] = [x for x in segments[4] if x in combi]
            segments[5] = [x for x in segments[5] if x in combi]
            segments[6] = [x for x in segments[6] if x not in combi]

    d = segments[3][0]
    a,b = segments[0]
    testA = all(a in x for x in len6)
    if testA:
        a,b = b,a
    c,g = segments[2]
    testG = all(g in x for x in len6)
    if testG:
        c,g = g,c
    e,f = segments[4]
    testF = all(f in x for x in len6)
    if testF:
        e,f = f,e
    
    zero = d + a + b + c + g + e
    one = a + b
    two = d + a + f + g + c
    three = d + a + f + b + c
    four = e + f + b + a
    five = d + e + f + b + c
    six = d + e + f + b + c + g
    seven = d + a + b
    eight = a + b + c + d + e + f + g
    nine = a + b + f + e + d + c

    N = {}

    N[''.join(sorted(zero))] = '0'
    N[''.join(sorted(one))] = '1'
    N[''.join(sorted(two))] = '2'
    N[''.join(sorted(three))] = '3'
    N[''.join(sorted(four))] = '4'
    N[''.join(sorted(five))] = '5'
    N[''.join(sorted(six))] = '6'
    N[''.join(sorted(seven))] = '7'
    N[''.join(sorted(eight))] = '8'
    N[''.join(sorted(nine))] = '9'

    op = output[i]
    o = [N[x] for x in op]
    num = int(''.join(o))
    part2 += num

print(part2)