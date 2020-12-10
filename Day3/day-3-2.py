"""
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

Your puzzle answer was 2832009600.
"""

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
