# Q: Count the unique paths from the top left to the bottom right.
# A single path may only move along 0's and can't visit the same 
# cell more than once.

# Matrix (2D Grid)
matrix = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


def unique_paths(grid, r, c, visit):
    ROWS = len(grid)
    COLS = len(grid[0])

    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or
        grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    

    visit.add((r,c))

    count = 0
    count += unique_paths(grid, r + 1, c, visit)
    count += unique_paths(grid, r - 1, c, visit)
    count += unique_paths(grid, r, c + 1, visit)
    count += unique_paths(grid, r, c - 1, visit)

    visit.remove((r,c))

    return count


print(unique_paths(matrix, 0, 0, set()))