from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    
    ROWS = len(grid)
    COLS = len(grid[0])

    visit = set()

    islands = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r,c))
        visit.add((r, c))

        while queue:
            row, col = queue.popleft()

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(ROWS) and c in range(COLS) and
                    grid[r][c] == '1' and (r, c) not in visit):
                    queue.append((r, c))
                    visit.add((r, c))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(r,c)
                islands += 1

    return islands



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
