# Find the length of the longest subarray with the same value in each position

my_nums = [4, 2, 2, 3, 3, 3]


def longest_subarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R-L + 1)
    return length


print(longest_subarray(my_nums))

#  Find the minimum length subarray where the suum is greater than  or equal to the target. Assume all values are positive


def shortestSubarray(nums, target):
    L = 0
    total = 0

    length = float("inf") # We are trying to minimisze it. When we ruun our min function, it would reduce it

    for R in range(len(nums)):
        total += nums[R]

        while total >= target:
            length = min(R-L+1, length)
            total -= nums[L]
            L += 1

    if length == float("inf"):
        return 0
    else:
        return length


print(shortestSubarray(my_nums, 5))
