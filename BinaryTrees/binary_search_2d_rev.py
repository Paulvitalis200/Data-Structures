def binary_search_2d(matrix, target):
    # Calculate number of rows and cols
    ROWS, COLS = len(matrix), len(matrix[0])
    # Check where the value lies in the matrix by comparing with the middle matrice
    top, bot = 0, ROWS - 1

    while top <= bot:
        mid = (top + bot) // 2

        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break


    # Do binary search on the respective matrice
    if not (top <= bot):
        return False
    
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(binary_search_2d(matrix, 8))