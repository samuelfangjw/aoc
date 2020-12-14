import math

f = open("input3.txt")

first = f.readline().split(',')
second = f.readline().split(',')

totalSteps = x = y = 0
dirX = [0, 1, 0, -1] # Up, Right, Down, Left
dirY = [1, 0, -1, 0]

vertices = {}

def getDirection(direction):
    if (direction == 'U'):
        return 0
    if (direction == 'R'):
        return 1    
    if (direction == 'D'):
        return 2
    if (direction == 'L'):
        return 3

for cmd in first:
    direction = getDirection(cmd[0])
    steps = int(cmd[1:])

    while (steps > 0):
        x += dirX[direction]
        y += dirY[direction]
        totalSteps += 1
        vertices[(x, y)] = totalSteps
        steps -= 1

totalSteps = x = y = 0
part1 = math.inf
part2 = math.inf

for cmd in second:
    direction = getDirection(cmd[0])
    steps = int(cmd[1:])

    while (steps > 0):
        x += dirX[direction]
        y += dirY[direction]
        totalSteps += 1
        if (x,y) in vertices:
            part1 = min(abs(x) + abs(y), part1)
            part2 = min(totalSteps + vertices[(x,y)], part2)
        steps -= 1

print("Part 1: {0}\nPart 2: {1}".format(part1, part2))