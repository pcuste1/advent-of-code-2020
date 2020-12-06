f = open("input.txt", "r")
lines = [ line.strip() for line in f ]

total = 0
curr = lines[0]

for i in range(0, len(lines)):
    if lines[i] == "":
        total += len(curr)
        curr = lines[i+1]
    else:
        temp = []
        for field in curr:
            if field in lines[i]:
                temp.append(field)
        curr = temp

total += len(curr)
print(total)