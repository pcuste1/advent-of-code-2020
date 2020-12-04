f = open("input.txt", "r")
board = [ [ col for col in row.strip() ] for row in f ]

num_rows = len(board)
num_cols = len(board[0])

num_trees = 0
col = 0
for row in range(0, num_rows):
    if board[row][col] == "#":
        num_trees += 1

    col = ( col + 3 ) % num_cols

print(num_trees)