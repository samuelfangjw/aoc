file = "input.txt"

with open(file) as f:
    input = [x.strip() for x in f.readlines()]
    nums = [int(x) for x in input[0].split(",")]
    input = [[int(y) for y in x.split()] for x in input[1:] if x]
    boards = []
    for i in range(len(input) // 5):
        boards.append(input[i * 5 : i * 5 + 5])

def win(board):
    return any(all(x in marked for x in row) for row in board) \
        or any(all(x in marked for x in [y[col] for y in board]) for col in range(5))

def calculate_score(board, num):
    unmarked = sum([sum([num for num in row if num not in marked]) for row in board])
    return unmarked * num

# Part 1
marked = set(nums[:4])
winning_board = -1

while winning_board == -1:
    marked.add(nums[len(marked)])
    for i, board in enumerate(boards):
        if win(board):
            winning_board = i
            break

part1 = calculate_score(boards[winning_board], nums[len(marked) - 1])

# Part 2
boards_left = list(range(len(boards)))
last_board = -1

while boards_left:
    marked.add(nums[len(marked)])
    boards_left = [x for x in boards_left if not win(boards[x])]
    if len(boards_left) == 1:
        last_board = boards_left[0]

part2 = calculate_score(boards[last_board], nums[len(marked) - 1])

print(part1)
print(part2)
