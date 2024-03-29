# Q. Count the number of  unique paths from  the top left to the  bottom right. You are only allowed to move down or to  the right.

#  Time complexity: O(2 ^ (n + m))
def brute_force(r, c, rows, cols):
    if r == rows or c == cols:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1

    return (brute_force(r+1, c, rows, cols) +
            brute_force(r, c+1, rows, cols))


print(brute_force(0, 0, 4, 4))


# Memoization - Time complexity: O(n * m)

def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = (memoization(r+1, c, rows, cols, cache) +
                   memoization(r, c+1, rows, cols, cache))

    return cache[r][c]


print(memoization(0, 0, 4, 4, [[0]*4 for i in range(4)]))


# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
def dp(rows, cols):
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]
        prevRow = curRow
    return prevRow[0]


print(dp(4, 4))
