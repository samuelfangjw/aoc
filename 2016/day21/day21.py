import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

SWAP_POS = 0
SWAP_LETTER = 1
ROTATE_BASED = 2
ROTATE = 3
REVERSE = 4
MOVE = 5

with open(file) as f:
    ops = []
    for line in f:
        line = line.strip().split()
        if line[0] == "swap":
            if line[1] == "position":
                ops.append((SWAP_POS, int(line[2]), int(line[5])))
            else:
                ops.append((SWAP_LETTER, line[2], line[5]))
        elif line[0] == "rotate":
            if line[1] == "based":
                ops.append((ROTATE_BASED, line[6], None))
            else:
                ops.append((ROTATE, line[1], int(line[2])))
        elif line[0] == "reverse":
            ops.append((REVERSE, int(line[2]), int(line[4])))
        elif line[0] == "move":
            ops.append((MOVE, int(line[2]), int(line[5])))

def scramble(txt):
    s = list(txt)
    for (op, x, y) in ops:
        if op == SWAP_POS:
            s[x], s[y] = s[y], s[x]
        elif op == SWAP_LETTER:
            x = s.index(x)
            y = s.index(y)
            s[x], s[y] = s[y], s[x]
        elif op == ROTATE_BASED:
            i = s.index(x)
            i += 1 + (1 if i >= 4 else 0)
            i %= len(s)
            s = s[-i:] + s[:-i]
        elif op == ROTATE and x == "left":
            s = s[y:] + s[:y]
        elif op == ROTATE and x == "right":
            s = s[-y:] + s[:-y]
        elif op == REVERSE:
            s[x:y+1] = s[x:y+1][::-1]
        elif op == MOVE:
            c = s.pop(x)
            s.insert(y, c)
    return "".join(s)

def unscramble(txt):
    s = list(txt)
    for (op, x, y) in ops[::-1]:
        if op == SWAP_POS:
            s[x], s[y] = s[y], s[x]
        elif op == SWAP_LETTER:
            x = s.index(x)
            y = s.index(y)
            s[x], s[y] = s[y], s[x]
        elif op == ROTATE_BASED:
            i = s.index(x)
            if i % 2 == 0 and i != 0:
                i = (i - 5) // 2
            else:
                i = i // 2 + 1
            i %= len(s)
            s = s[i:] + s[:i]
        elif op == ROTATE and x == "left":
            s = s[-y:] + s[:-y]
        elif op == ROTATE and x == "right":
            s = s[y:] + s[:y]
        elif op == REVERSE:
            s[x:y+1] = s[x:y+1][::-1]
        elif op == MOVE:
            c = s.pop(y)
            s.insert(x, c)
    return "".join(s)

print("Part 1:", scramble("abcdefgh"))
print("Part 2:", unscramble("fbgdceah"))
