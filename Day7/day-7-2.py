def recursive_contains(color, bags):
    total = 1
    for key, value in bags[color].items():
        if value != "n":
            total += int(value) * recursive_contains(key, bags)
    return total

f = open("input.txt", 'r')
bags = {}

for line in f:
    color, contents = line.split(" bags contain ")
    contained = {}
    for inner in contents.strip(".\n").split(", "):
        innter_color = inner[2:].split(" bag")[0]
        contained[innter_color] = inner[0]
     
    bags[color] = contained

total = recursive_contains("shiny gold", bags) - 1
print(total)