import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
contents = open(file).read().strip()

idx = 0
count1 = 0

while idx < len(contents):
    if contents[idx] == '(':
        start_idx = idx
        while contents[idx] != ')':
            idx += 1
        s = contents[start_idx + 1: idx]
        n, r = s.split("x")
        count1 += int(n) * int(r)
        idx += int(n) + 1
    else:
        count1 += 1
        idx += 1

print(count1)

def get_total(idx, end):
    count = 0
    while idx < end:
        if contents[idx] == '(':
            start_idx = idx
            while contents[idx] != ')':
                idx += 1
            s = contents[start_idx + 1: idx]
            n, r = s.split("x")
            count += get_total(idx + 1, idx + 1 + int(n)) * int(r)
            idx += int(n) + 1
        else:
            idx += 1
            count += 1

    return count

count2 = get_total(0, len(contents))
print(count2)
