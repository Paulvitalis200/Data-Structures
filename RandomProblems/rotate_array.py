def rotate(nums, k):
    k = k % len(nums)

    # if k is length of input array, we are not
    # if k is greater than the llength we mode it

    i, j = 0, len(nums) - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

    i, j = 0, k - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

    i, j = k, len(nums) - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1
