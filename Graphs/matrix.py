# Count paths backtracking
# Matrix (2D Grid)
from collections import deque
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


def dfs(grid, r, c, visit):
    # Get dimensions of the matrix
    ROWS, COLS = len(grid), len(grid[0])

    # BASE CASES
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        grid[r][c] == 1 or
            (r, c) in visit):
        return 0

    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r, c - 1, visit)
    count += dfs(grid, r, c + 1, visit)

    visit.remove((r, c))
    return count


print(dfs(grid, 0, 0, set()))


# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right


def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
