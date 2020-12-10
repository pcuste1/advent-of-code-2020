f = open("input.txt", "r")

adapters = [int(line.strip()) for line in f]
adapters.append(0)
adapters.sort()

permutations = [0]*len(adapters)
permutations[-1] = 1

def connect_adapters(index, adapters):
    # check if we've already calculated the permutations for this index
    if permutations[index] != 0:
        return permutations[index]
    
    # loop over the 3 next elements, the 4th is guaranteed to be too large 
    # since the list is sorted
    for i in range(1,min(4, len(adapters) - index)):
        if adapters[index + i] - adapters[index] <= 3:
            permutations[index] += connect_adapters(index+i, adapters)

    return permutations[index]

print(connect_adapters(0, adapters))