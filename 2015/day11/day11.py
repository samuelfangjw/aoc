import re

input= "hxbxwxba"

def inc(pw):
    # Inspired by solution on https://www.reddit.com/r/adventofcode/comments/3wbzyv/day_11_solutions/
    return re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1))+1) + len(x.group(2)) * "a", pw)

def test(pw):
    triplets = list(zip(pw[:-2], pw[1:-1], pw[2:]))
    cond1 = any([ord(x) == ord(y) - 1 == ord(z) - 2 for x,y,z in triplets])
    cond2 = 'i' in pw or 'o' in pw or 'l' in pw
    pairs = list(dict.fromkeys(zip(pw[:-1], pw[1:])))
    cond3 = sum([1 if x == y else 0 for x,y in pairs]) >= 2
    return cond1 and not cond2 and cond3

def next(pw):
    while not test(pw):
        pw = inc(pw)
    return pw

# Part 1
input = next(input)
print(input)

# Part 2
input = inc(input)
input = next(input)
print(input)
