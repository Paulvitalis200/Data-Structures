
def prefix_sum(nums, L, R):
    total = 0
    prefix = []

    for n in nums:
        total += n
        prefix.append(total)

    def sum_query(L, R):
        preRight = prefix[R]
        preLeft = prefix[L - 1] if L > 0 else 0
        return (preRight - preLeft)
    
    return sum_query(L, R)

print(prefix_sum([2,3,-1,9,-5,3,8, -10, 3, 19], 3, 8))