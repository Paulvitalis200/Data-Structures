# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

def longest_turbulent_subarray(nums):
    l, r = 0, 1
    res, prev = 1, ""

    while r < len(nums):
        if nums[r - 1] > nums[r] and prev != ">":
            res = max(res, r - l + 1)
            r += 1
            prev = ">"
        elif nums[r - 1] < nums[r] and prev != "<":
            res = max(res, r - l + 1)
            r += 1
            prev = "<"
        else:
            r = r + 1 if nums[r] == nums[r - 1] else r
            l = r - 1
            prev = ""
    
    return res
