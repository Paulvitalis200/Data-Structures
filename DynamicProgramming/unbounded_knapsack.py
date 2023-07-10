# Given a list of N items, and a backpack  with a limited capacity, return the maximum
#  total  profit  that can be contained in  the backpack.  The i-th item's profit is profit[i
# ] and it's weight is weight[i].  Assume you can only add each item to the bag at most one time

# Time  : O(2^C), space: O(C)
def dfs(profit, weight,  capacity):
    return dfsHelper(0, profit, weight, capacity)


def dfsHelper(i, profit, weight, capacity):
    # Base case
    if i == len(profit):
        return 0

    # skip item  i
    max_profit = dfsHelper(i+1, profit, weight, capacity)

    # include item i

    newCap = capacity - weight[i]

    if newCap >= 0:
        p = profit[i] + dfsHelper(i, profit, weight,  newCap)
        # Compute the max
        max_profit = max(profit, p)

    return max_profit

# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.


def memoization(profit, weight, capacity):
    # A 2d array, with N rows and M + 1 columns, init with -1's
    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)


def memoHelper(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]

    # Skip item i
    cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)

    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + memoHelper(i, profit, weight, newCap, cache)
        # Compute the max
        cache[i][capacity] = max(cache[i][capacity], p)

    return cache[i][capacity]
