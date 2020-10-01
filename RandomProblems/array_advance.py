# ARRAY ADVANCE GAME
### You are given an array of non-negative integers. For example:

# [3,3,1,0,2,0,1]
# Each number represents the maximum yoou cann advance in the array
# Question:
# Is it possible to advance from the start of the array to the last element?

# Example (Approach 1)

# Use "greedy" strategy. Advance as much as possible for each
# number. (Note this will not work)

# (Approach 2)

# Iterate through each entry in array
# Track furthest we can reach from entry  (A[i]+i)
# If for some "i" before the end is the furthest that wee can reach,
# we can't reach the last index. Otherwise, the end is reached.

# i: index processed
# Furthest possible to advance from "i": A[i]+i

def array_advance(A):

    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    
    return furthest_reached >= last_idx

A1 = [3,3,1,0,2,0,1]
print(array_advance(A1))

A2 = [3,2,0,0,2,0,1]
print(array_advance(A2))