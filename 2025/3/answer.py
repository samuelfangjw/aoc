import sys

lines = []

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip().split("\n")
    for line in data:
        lines.append([int(x) for x in line])


def get_val(x):
    ans = 0
    for digit in x:
        ans = ans * 10 + digit
    return ans


def solve(n):
    res = 0
    for line in lines:
        ans = [0] * n
        for x in line:
            new_ans = ans[:]
            for i in range(n):
                candidate = ans[:i] + ans[i + 1 :] + [x]
                if get_val(candidate) > get_val(new_ans):
                    new_ans = candidate
            ans = new_ans

        res += get_val(ans)
    return res


print("Part 1:", solve(2))
print("Part 1:", solve(12))
