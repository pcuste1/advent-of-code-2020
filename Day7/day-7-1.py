class Bag():
    def __init__(self, color, contents):
        self.color = color
        self.contents = {}
        for inner in contents.strip(".\n").split(", "):
            color = inner[2:].split(" bag")[0]
            self.contents[color] = inner[0]

    def can_contain(self, color):
        return self.contents.get(color) != None

prev_chosen = []
def recursive_contains(color, bags):
    total = 0
    for bag in bags:
        if not(bag.color in prev_chosen) and bag.can_contain(color):
            prev_chosen.append(bag.color)
            total += 1 + recursive_contains(bag.color, bags)
    return total

f = open("input.txt", 'r')
bags = []
for line in f:
    color, contents = line.split(" bags contain ")
    bags.append(Bag(color, contents))

total = recursive_contains("shiny gold", bags)
print(total)