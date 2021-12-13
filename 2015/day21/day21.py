import math

EHP = 103
ED = 9
EA = 2
HP = 100

weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74, 8, 0)]
armor = [(0,0,0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

rings_combi = list(set([(x[0]+y[0], x[1]+y[1], x[2]+y[2]) for x in rings for y in rings if x != y] + rings))

win = []
lose = []

for w in weapons:
    for a in armor:
        for r in rings_combi:
            P = w[0] + a[0] + r[0]
            D = w[1] + a[1] + r[1]
            A = w[2] + a[2] + r[2]
            if math.ceil(EHP / max(D - EA, 1)) <= math.ceil(HP / max(ED - A, 1)):
                win.append(P)
            else:
                lose.append(P)

print(min(win))
print(max(lose))
