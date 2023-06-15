def binary_search(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid

    return -1


print(binary_search([-1, 0, 3, 5, 9, 12], 9))
