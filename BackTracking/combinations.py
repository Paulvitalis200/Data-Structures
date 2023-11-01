# Given two numbers n and k, return all posssible combination of size=k, choosing  from values between 1 and n.
#  Time: O(k * 2^n)
def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)

    return combs

def helper(i, curComb, combs,  n, k):
    if  len(curComb) == k:
        combs.append(curComb.copy())
        return
    
    if i > n:
        return
    
    # Decision to incllude i
    curComb.append(i)
    helper(i+1, curComb, combs, n, k)
    curComb.pop()

    # Decision to NOT include i
    helper(i, curComb, combs, n, k)


# Tiime: O(k * C(n, k))
def combinations2(n,k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    
    if i > n:
        return
    
    for j in range(i, n+1):
        curComb.append(i)
        helper2(j+1, curComb, combs, n, k)
        curComb.pop()