
def searchMatrix(matrix, target: int) -> bool:
    # Get dimensions. No of ROWS and COLS
    ROWS, COLS = len(matrix), len(matrix[0])

    # We now do our first binary search
    # Now look for the row we need to find
    # top - Top row
    # bot - Bottom row
    top, bot = 0, ROWS - 1

    while top <= bot:
        row = (top + bot) // 2

        # Compare target value with the right most value in the row
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    # If none of the rows contain the target value
    if not (top <= bot):
        return False
    
    # Get the middle matrix row
    row = (top + bot) //2

     # Do binary search on the respective matrice
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) //2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

searchMatrix(matrix, 3)