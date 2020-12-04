f = open("input.txt", "r")
board = [ [ col for col in row.strip() ] for row in f ]

num_rows = len(board)
num_cols = len(board[0])

def count_trees(row_moves, col_moves):
    num_trees = 0
    col = 0
    for row in range(0, num_rows, row_moves):
        if board[row][col] == "#":
            num_trees += 1

        col = ( col + col_moves ) % num_cols

    return num_trees

total = count_trees(1,1) * count_trees(1,3) * count_trees(1,5) * count_trees(1,7) * count_trees(2,1)

print(total)
