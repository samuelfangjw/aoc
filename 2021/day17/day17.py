# target area: x=265..287, y=-103..-58
target_x = range(265, 287 + 1)
target_y = range(-103, -58 + 1)

start = (0,0)

def move(curr, dx, dy):
    x,y = curr
    return (x + dx, y + dy)

max_y = 0
distinct = set()
for i in range(288):
    for j in range(-104, 104):
        dx, dy = i, j
        x, y = 0,0
        curr = 0
        while True:
            if x in target_x and y in target_y:
                max_y = max(curr, max_y)
                distinct.add((i,j))
                break
            elif x > 287 or y < -103:
                break
            else:
                x += dx
                y += dy
                curr = max(y, curr)
                dy -= 1
                dx -= 1
                dx = max(dx, 0)

print(max_y)
print(len(distinct))
