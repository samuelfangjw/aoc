import sys
from itertools import combinations
from z3 import Solver, Real

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
points = []

with open(file) as f:
    for line in f:
        line = line.strip()
        a,b = line.split(' @ ')
        px,py,pz = a.split(', ')
        vx,vy,vz = b.split(', ')
        points.append(list(map(int,[px,py,pz,vx,vy,vz])))

def intersect(p1, p2):
    px1,py1,_,vx1,vy1,_ = p1
    px2,py2,_,vx2,vy2,_ = p2

    a1 = vy1
    b1 = -vx1
    c1 = a1*(px1) + b1*(py1)
 
    a2 = vy2
    b2 = -vx2
    c2 = a2*(px2) + b2*(py2)
 
    determinant = a1*b2 - a2*b1

    if determinant == 0:
        return [None, None]
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant

        if (x-px1)/vx1 < 0 or (y-py1)/vy1 < 0 or (x-px2)/vx2 < 0 or (y-py2)/vy2 < 0:
            return [None, None]

        return [x, y]

part1 = 0
min_bound,max_bound = 200000000000000,400000000000000

for i, j in combinations(range(len(points)), 2):
    p1,p2 = points[i], points[j]
    x,y = intersect(p1,p2)

    if x is None:
        continue

    if min_bound<=x<=max_bound and min_bound<=y<=max_bound:
        part1 += 1

# part 2 adapted from: https://github.com/Rankail/aoc2023/blob/master/py/24/2.py
solver = Solver()

for i, (px,py,pz,vx,vy,vz) in enumerate(points[:3]):
    t = Real(f"t{i}")
    solver.add(t >= 0)
    solver.add(Real("x") + Real("vx") * t == px + vx * t)
    solver.add(Real("y") + Real("vy") * t == py + vy * t)
    solver.add(Real("z") + Real("vz") * t == pz + vz * t)

solver.check()
model = solver.model()
rx, ry, rz = model.eval(Real("x")).as_long(), model.eval(Real("y")).as_long(), model.eval(Real("z")).as_long()

part2 = rx + ry + rz

print(part1, part2)
