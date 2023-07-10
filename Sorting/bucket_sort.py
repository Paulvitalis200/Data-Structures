# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


def sort(nums):
    counts = [0, 0, 0]

    for i in range(len(nums)):
        counts[nums[i]] += 1

    i = 0
    for n in range(len(counts)):
        for _ in range(counts[n]):
            nums[i] = n
            i += 1

    return nums


print(sort([0, 2, 1, 2, 0, 1, 2, 1, 0]))
