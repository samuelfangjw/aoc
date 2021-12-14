import hashlib

door_id = "wtnhxymk"

# Part 1
idx = 0
part1 = ""

while True:
    if len(part1) == 8:
        break
    hash = hashlib.md5((door_id + str(idx)).encode()).hexdigest()
    if hash[:5] == "00000":
        part1 += hash[5]
    idx += 1

print(part1)

#  Part 2
idx = 0
visited = [False] * 8
part2 = [0] * 8

while True:
    if all(visited):
        break
    hash = hashlib.md5((door_id + str(idx)).encode()).hexdigest()
    if hash[:5] == "00000" and hash[5].isnumeric():
        pos = int(hash[5])
        if 0 <= pos < 8 and not visited[pos]:
            part2[pos] = hash[6]
            visited[pos] = True
    idx += 1

print("".join(part2))
    