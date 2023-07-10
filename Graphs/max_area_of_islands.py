def maxArea(grid):

    ROWS, COLS = len(grid), len(grid[0])

    visit = set()

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(grid, r, c, ROWS,  COLS, visit))

    return area


def dfs(grid, r, c, ROWS, COLS, visit):
    if (r < 0 or r == ROWS or
        c < 0 or c == COLS or
            (r, c) in visit or grid[r][c] == 0):
        return 0

    visit.add((r, c))

    return (1 + dfs(grid, r + 1, c, ROWS, COLS, visit) +
            dfs(grid, r - 1, c, ROWS, COLS, visit) +
            dfs(grid, r, c+1, ROWS, COLS, visit) +
            dfs(grid, r, c - 1, ROWS, COLS, visit))


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(maxArea(grid))
