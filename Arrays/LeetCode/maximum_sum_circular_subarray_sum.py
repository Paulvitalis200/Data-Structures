def max_circular(nums):
    curMax, curMin = 0, 0
    globalMax, globalMin = nums[0], nums[0]
    
    total = 0

    for n in nums:
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globalMax = max(globalMax, curMax)
        globalMin = min(globalMin, curMin)


    # If return globalMax, we know it ran through the middle
    # If circular, total - globalMin.
    # Edge case is when all our numbers are negative and thus globalMax < 0. 
    # Meaning we have no positive integer [-5, -3, -5], Meaning we 
    # return globalMax because total - globalMin ie -13 - -13 = 0. We can't return 0
    return max(globalMax, total - globalMin) if globalMax > 0 else globalMax