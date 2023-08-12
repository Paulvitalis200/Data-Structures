
# Given an array, retuurn true if there are two elements within  a window of sixe k that  are equal


# Method 1: Bruteforce - Time complexity = O(n^2)

myArray = [4, -1, -2, -7, 3, 4]
myArray2 = [1, 2, 3, 2, 3, 3]


def brute_force(nums, k):

    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


print(brute_force(myArray2, 3))

# Method 2: Use of Hashset


def containsDups(nums, k):
    window = set()

    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True

        window.add(nums[R])

    return False


print(containsDups(myArray2, 3))
