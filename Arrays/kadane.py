# Find a non empty subarray with the largest sum

myArray = [4, -1, -2, -7, 3, 4]

# Brute force - O(n^2)


def brute_force(nums):

    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)

    return max_sum


print(brute_force(myArray))


# Kadane's  - O(n)

def kadane(nums):
    max_sum = nums[0]
    cur_sum = 0

    for i in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += i
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(kadane(myArray))

# Kadane sliding window - O(n)


def kadane_sliding_window(nums):
    max_sum = nums[0]
    cur_sum = 0
    L, R = 0, 0
    maxL, maxR = L, R

    for R in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += nums[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            maxL, maxR = L, R

    return [maxL, maxR]


print(kadane_sliding_window(myArray))
