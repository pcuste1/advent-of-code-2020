def bin_search(moves, nodes, lower_branch):
    for move in moves:
        middle_point = len(nodes) // 2
        if move == lower_branch:
            nodes = nodes[:middle_point]
        else:
            nodes = nodes[middle_point:]
    return nodes[0]

def det_row(row_id):
    return bin_search(row_id, list(range(0,128)), "F")

def det_col(col_id):
    return bin_search(col_id, list(range(0,8)), "L")

f = open("input.txt", "r")

boarding_ids = []
for line in f:
    row_id = det_row(line[:7])
    col_id = det_col(line[7:])
    boarding_ids.append(row_id * 8 + col_id)

boarding_ids.sort()
for i in range(0,len(boarding_ids)-1):
    if boarding_ids[i+1] - boarding_ids[i] == 2:
        print(boarding_ids[i] + 1)