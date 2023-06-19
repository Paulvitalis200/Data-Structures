# Given a list of N items, and a backpack  with a limited capacity, return the maximum
#  total  profit  that can be contained in  the backpack.  The i-th item's profit is profit[i
# ] and it's weight is weight[i].  Assume you can only add each item to the bag at most one time


def dfs(profit, weight, capacity):
    return dfshelper(0, profit, weight, capacity)


def dfshelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # skip item i
    maxProfit = dfshelper(i+1, profit, weight, capacity)

    # include item i
    newCap = capacity - weight[i]

    if newCap >= 0:
        p = profit[i] + dfshelper(i + 1, profit, weight, newCap)
        # Compute the max
        maxProfit = max(p, maxProfit)

    return maxProfit
