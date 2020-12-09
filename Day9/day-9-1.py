def contains_sum(target, values):
    for x in range(0, 25):
        for y in range(x+1, 25):
            if values[x] + values[y] == target:
                return True
    return False

f = open("input.txt", "r")

lines = [ int(line.strip()) for line in f]

for i in range(25, len(lines)):
    if not contains_sum(lines[i], lines[i-25:i]):
        print(lines[i])
        break