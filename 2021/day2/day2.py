# Part 1
with open("input.txt") as f:
    ip = [line.split() for line in f.readlines()]
    depth = sum([int(y) if x == "down" else -int(y) if x == "up" else 0 for (x,y) in ip])
    horiz = sum([int(y) if x == "forward" else 0 for (x,y) in ip])
    
    output1 = depth * horiz
    print(output1)

# Part 2
with open("input.txt") as f:
    depth = 0
    horiz = 0
    aim = 0
    for line in f:
        x, y = line.split()
        
        if (x == "down"):
            aim = aim + int(y)
        
        if (x == "up"):
            aim = aim - int(y)
        
        if (x == "forward"):
            horiz = horiz + int(y)
            depth = depth + aim * int(y)
    
    output2 = depth * horiz
    print(output2)