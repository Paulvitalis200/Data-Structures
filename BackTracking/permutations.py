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

print(permutationsIterative([2,3,4]))