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
