def find_contiguous(target, values):
    curr = []
    for x in values:
        # make a rolling shutter and pop from beginning when sum gets too large
        curr.append(x)
        while(sum(curr) > target):
            curr.pop(0)
        if sum(curr) == target:
            return curr

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
        contiguous = find_contiguous(lines[i], lines[:i])
        contiguous.sort()
        encryption_weakness = contiguous[0] + contiguous[-1]
        print(encryption_weakness)
        break