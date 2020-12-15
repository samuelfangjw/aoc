# INPUT 240298-784956
a = 240298
b = 784956

def checkPart1(x):
    prev = '0'
    repeat, increasing= False, True

    for c in x:
        repeat = c == prev or repeat

        if c < prev:
            increasing = False
            break
        prev = c

    return repeat & increasing

def checkPart2(x):
    prev = '0'
    prev2 = ''
    repeat, increasing= False, True

    for i in range(len(x)):
        if x[i] == prev and prev != prev2 and not repeat:
            repeat = True
            if i+1 != len(x) and x[i+1] == prev:
                repeat = False

        if x[i] < prev:
            increasing = False
            break

        prev2 = prev
        prev = x[i]

    return repeat & increasing

count1 = count2 = 0
for x in range(a, b + 1):
    x = str(x)
    count1 += checkPart1(x)
    count2 += checkPart2(x)

print("Part 1: {0}\nPart 2: {1}".format(count1, count2))