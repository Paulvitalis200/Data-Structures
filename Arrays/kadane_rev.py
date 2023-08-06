# Given an array, find the maximum sum subarray

nums  = [-3,4, 7, -18, 23, 55, -2, 84, 1]

# Time complexity - O(n^2)

def brute_force(arr):
    if len(arr) == 0:
        return
    
    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0

        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)

    return max_sum

# Time complexity - O(n)
def kadane(arr):
    if len(arr) == 0:
        return
    
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(cur_sum, max_sum)

    return max_sum

def kadane_sliding_window(arr):
    if len(arr) == 0:
        return
    
    max_sum = arr[0]
    cur_sum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(arr)):
        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += arr[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            maxL, maxR = L, R

    return [maxL, maxR]


print(kadane(nums))
print(kadane_sliding_window(nums))