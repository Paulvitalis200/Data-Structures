# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        q = deque()
        # time to keep track of how much time has passed
        # keep track of how many fresh oranges we have at any given time
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        # Iterate over gridd to do prework
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                # identify rotting oranges and add them to queue to run bffs
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1], [0,-1], [1,0],[-1,0]]
        while q and fresh > 0:

            # To add adjacent oranges to our queue marking them as rotten
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue

                    grid[row][col] = 2

                    q.append([row, col])
                    #decremnt fresh oranges
                    fresh -= 1
            
            # increment time
            time += 1
        # how do we know to return time or negative -1. If fresh == 0, mmeaning we made every orange rotten
        return time if fresh == 0 else -1




        