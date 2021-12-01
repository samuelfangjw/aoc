# Part 1
f = [int(x) for x in open("input.txt")]

prev = 0
count = -1

for num in f:
    if num > prev:
        count = count + 1
    prev = num

print(count)

# Part 2
prev = 0
count = -1
l = 0

while l < len(f) - 2:
    window = f[l] + f[l + 1] + f[l + 2]
    if window > prev:
        count = count + 1
    prev = window
    l = l + 1

print(count)