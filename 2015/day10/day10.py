input = "1321131112"

for i in range(50):
    newStr = ""
    count = 0
    prev = input[0]
    for i in range(len(input)):
        if input[i] == prev:
            count = count + 1
        else:
            newStr += str(count) + prev
            count = 1
            prev = input[i]
    newStr += str(count) + prev
    input = newStr

part1 = len(input)
print(part1)
