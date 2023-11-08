def permutationsRecursive(nums):
    return helper(0, nums)

def helper(i, nums):
    if i == len(nums):
        return [[]]
    
    resPerms = []
    perms = helper(i+1, nums)
    print(perms)
    for  p  in  perms:
        for j in  range(len(p) +  1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms

def  permutationsIterative(nums):
    perms = [[]]

    for  n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p)+1):
                pCopy = p.copy()

                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms


def permuteUnique(nums):
    #  [1,1,3,4,2,1]
    res = []
    perms = []
    count = {n:0 for n in nums}

    for n in nums:
        count[n] += 1

    def dfs():
        if len(perms) == len(nums):
            res.append(perms.copy())
            return

        for n in count:
            if count[n] > 0:
                perms.append(n)
                count[n] -= 1

                dfs()

                count[n] += 1
                perms.pop()
            # will ensure. no duplicates and we get every single perm

    dfs()
    return res

print(permutationsIterative([2,3,4]))