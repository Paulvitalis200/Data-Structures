# Find a non empty subarray with the largest sum

myArray = [4, -1, -2, -7, 3, 4]

# Brute force - O(n^2)


def brute_force(nums):
    if len(nums) == 0:
        return

    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0

        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(cur_sum, max_sum)
    
    return max_sum


# Kadane's  - O(n)

def kadane(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum

# Kadane sliding window - O(n)


def kadane_sliding_window(nums):
    max_sum = nums[0]
    cur_sum = 0
    maxR, maxL = 0, 0
    L = 0

    for R in range(nums):
        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += nums[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            maxL, maxR = L, R

    return [maxL, maxR]


print(kadane_sliding_window(myArray))

def max_sub_array_circular(nums):
    globalMax, globalMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0

    for n in nums:
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        globalMax = max(curMax,  globalMax)
        globalMin = min(globalMin, curMin)
        total += n
    
    if globalMax > 0:
        return max(globalMax, total - globalMin)
    return globalMax
