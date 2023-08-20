# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

def min_size_subarray(nums, target):
    L, total = 0,0
    length = float("inf")

    for  R in  range(len(nums)):
        total += nums[R]

        while total >= target:
            length = min(length, R-L+1)
            total -= nums[L]
            L += 1
    
    return 0 if length == float("inf") else length

print(min_size_subarray([2,3,1,2,4,3], 7))