k = 2
ans = 20151125
target_row = 2978
target_col = 3083

FOUND = False
while True:
    if FOUND:
        break
    for i in range(k,0,-1):
        row = i
        col = k-i+1
        ans = (ans * 252533) % 33554393
        if row == target_row and col == target_col:
            print(ans)
            FOUND = True
            break  
    k += 1
