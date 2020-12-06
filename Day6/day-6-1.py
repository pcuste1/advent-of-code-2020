f = open("input.txt", "r")
lines = [ line.strip() for line in f ]

total = 0
curr = []
for line in lines:
    if line == "":
        total += len(curr)
        curr = []
    else:
        for field in line:
            if not(field in curr):
                curr.append(field)

total += len(curr)
print(total)