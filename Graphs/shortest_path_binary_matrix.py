# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.



from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        # Get dimensions. Square grid
        N = len(grid)
        queue = deque([(0,0, 1)])
        visit = set()
        visit.add((0,0))
        directions = [[0,1],[1,0], [0, -1], [-1, 0],
                    [1,1],[-1,-1], [1, -1], [-1, 1]]

        while queue:
            r, c, length = queue.popleft()
            # its okay if a node has been visited. We still need to process it. 
            # We make sure we dont process a node multiple times. we dont incluude this in check (r,c ) in visit
            if (min(r, c) < 0 or max(r, c) == N or grid[r][c] == 1):
                continue
            
            if r == N- 1 and c == N -1:
                return length

            for dr, dc in directions:
                # we dont want to visit nodes that we've already visited before
                if (r+dr, c+dc) not in visit: 
                    queue.append((r+dr, c+dc, length+1))
                    visit.add((r+dr, c+dc))
        return -1
        
