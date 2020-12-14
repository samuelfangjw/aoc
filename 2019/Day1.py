f = open("input1.txt")
sumPart1 = sumPart2 = 0
for x in f:
    fuel = int(x) // 3 - 2
    sumPart1 += fuel
    
    while (fuel > 0):
        sumPart2 += fuel
        fuel = fuel // 3 - 2

print("Part 1: {0}\nPart 2: {1}".format(sumPart1, sumPart2))