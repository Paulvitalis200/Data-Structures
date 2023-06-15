# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
# n = 10, pick = 6
# n = 1, pick = 1

def guessNumber(self, n: int) -> int:
    l = 1
    r = n

    while l < r:
        mid = (l + r) // 2
        res = guess(mid)

        if res > 0:
            l = mid + 1
        elif res < 0:
            r = mid - 1
        else:
            return mid


def guess(num, pick):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0
