import sys
import math

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.readline().strip()

pkt = bin(int(data, 16))[2:].zfill(len(data) * 4)

part1 = 0
part2 = []

def parse(pkt):
    global part1
    V = int(pkt[0:3],2)
    part1 += V
    T = int(pkt[3:6],2)
    
    if T == 4:
        idx = 6
        num = ""
        num += pkt[idx+1:idx+5]
        while pkt[idx] == '1':
            idx += 5
            num += pkt[idx+1:idx+5]
        idx += 5
        part2.append(int(num,2))
        return idx
    else:
        I = int(pkt[6],2)
        num_pkts = 0
        if I == 0:
            i = 22
            L = int(pkt[7:i],2)
            l = 0
            while l < L:
                num_pkts += 1
                l += parse(pkt[i+l:])
        else:
            i = 18
            L = int(pkt[7:i],2)
            l = 0
            num_pkts = L
            for _ in range(L):
                l += parse(pkt[i+l:])
        
        vals = []
        for _ in range(num_pkts):
            vals.append(part2.pop())
        if T == 0:
            part2.append(sum(vals))
        elif T == 1:
            part2.append(math.prod(vals))
        elif T == 2:
            part2.append(min(vals))
        elif T == 3:
            part2.append(max(vals))
        else:
            if T == 5:
                f = lambda x,y: x > y
            elif T == 6:
                f = lambda x,y: x < y
            elif T == 7:
                f = lambda x,y: x == y
            part2.append(int(f(vals[1],vals[0])))
        return i + l

parse(pkt)

print(part1)
print(part2[0])
