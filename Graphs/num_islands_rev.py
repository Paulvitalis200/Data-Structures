
from collections import deque


def numIslands(grid):
    if grid is None:
        return 0

    R, C = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(R):
        for c in range(C):
            if (grid[r][c] == "1" and (r, c) not in visited):
                bfs(grid, r, c, R, C, visited)
                islands += 1

    return islands


def bfs(grid, r, c, rows, cols, visited):

    queue = deque()
    queue.append((r, c))
    visited.add((r, c))

    while queue:

        row, col = queue.popleft()

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if ((r) in range(rows) and
                (c) in range(cols) and
                (r, c) not in visited and
                    grid[r][c] == '1'):
                queue.append((r, c))
                visited.add((r, c))


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))

print(numIslands(grid2))
