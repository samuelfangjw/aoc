import hashlib

input = "iwrupvqb"

# Part 1
part1 = 1
while hashlib.md5((input + str(part1)).encode()).hexdigest()[0:5] != "00000":
    part1 += 1

print(part1)

# Part 2
part2 = 1
while hashlib.md5((input + str(part2)).encode()).hexdigest()[0:6] != "000000":
    part2 += 1

print(part2)
    