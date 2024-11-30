import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

def solve(total):
    prev_row = (["."] + list(data) + ["."])
    curr_row = ["."] * len(prev_row)
    safe = prev_row.count(".") - 2

    for _ in range(1, total):
        for col in range(1, len(curr_row) - 1):
            left, center, right = prev_row[col-1:col+2]

            if left == "^" and center == "^" and right == ".":
                curr_row[col] = "^"
            elif center == "^" and right == "^" and left == ".":
                curr_row[col] = "^"
            elif left == "^" and center == "." and right == ".":
                curr_row[col] = "^"
            elif right == "^" and center == "." and left == ".":
                curr_row[col] = "^"
            else:
                curr_row[col] = "."
                safe += 1

        prev_row = curr_row
        curr_row = ["."] * len(prev_row)
    return safe

print("Part 1:", solve(40))
print("Part 2:", solve(400000))
