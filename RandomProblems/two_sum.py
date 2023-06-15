# Given a sorted array of integers, return the two numbers such that
#  they add up to a specific target. You may assume that each  input
#  would have  exactly  one solution, and  you may not use  the  same element twice

A = [-2, 1, 2, 4, 7, 11]
target = 5

# Time Complexity: O(n^2)
# Space Complexity: O(1) We're not using  any auxiliary data structures to store anything.
# We're just looping through to checkt the sum


def two_sum_brute_force(A,  target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

# A = [-2, 1, 2, 4, 7, 11]
# target = 5

# i = 0
# ht  = {}
# ht[7] = -2

# i = 1
# ht[4] = 1

# i = 2
# ht[3] = 2

# i = 3

# Time Complexity:  O(n) Linear
# Space Complexity: O(n) - Storing the dictionary and its proportional to the number of items


def two_sum_hash_table(A, target):
    hash_table = dict()
    for i in range(len(A)):
        if A[i] in hash_table:
            print(hash_table[A[i]], A[i])
            return True
        else:
            hash_table[target - A[i]] = A[i]
    return False

# Time complexity: O(n) - n = size of given array
# Space  complexity: O(1) - Not storing anything
#  Takes advantage that  the array is sorted


def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


def two_sum_latest(A, target):
    hash_map = {}

    for i, n in enumerate(A):
        diff = target - n
        if diff in hash_map:
            return [hash_map[diff], i]
        else:
            hash_map[n] = i
    return


# print(two_sum_brute_force(A, target))
# print(two_sum_hash_table(A, target))
print(two_sum(A, target))
print(two_sum_latest(A, target))
