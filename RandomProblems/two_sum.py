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

print(two_sum_brute_force(A, target))