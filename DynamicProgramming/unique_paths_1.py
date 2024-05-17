# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n

        prevRow = [0] * n

        for r in range(rows - 1, -1, -1):
            curRow = [0] * n
            curRow[cols - 1] = 1

            for c in range(cols - 2, -1, -1):
                curRow[c] = curRow[c+ 1] + prevRow[c]

            prevRow = curRow

        return prevRow[0]
