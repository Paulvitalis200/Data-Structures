class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

        # total - Total value of a node
        # left, right = left and right children - they'll be pointers
        #L, R refer to the left and right boundaries of a node


    #O(n)
    @staticmethod
    def build(nums, L, R):
        # Given an array (nums) and two boundaries (L and R) 
        # We want to break that array into smaller arrayss by hallf
        # and create nodes for each portion

        #Base case - where we have a range of 1 and L and R are equal
        if L == R:
            # We create a segment tree node
            # Total value is the value of the nums array at that position
            return SegmentTree(nums[L], L, R)
        
        # if no base case
        M = (L + R) // 2
        # Create temp root node. We don't know total val yet. Total we put 0. But ffor left, right we put 0, 5
        root = SegmentTree(0, L, R)
        
        # Build left side of segment tree recursively and assignn to root.left
        root.left = SegmentTree.build(nums, L, M)

        # Build right side of segment tree
        root.right = SegmentTree.build(nums, M+1, R)
        
        # Calculate  sum of root node by taking left and right sums
        root.sum = root.left.sum + root.right.sum

        return root

    # O(logn)

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index,val)

        # Update sum of the tree after the update
        self.sum = self.left.sum + self.right.sum

    # O(log n)
    def rangeQuery(self,  L, R):
        # [ 4,3,1,3,1]
        # Starting case where: L = 0, R = 5
        if L == self.L and R == self.R:
            return self.sum
        
        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(L,R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return (self.left.rangeQuery(L, M) +
                    self.right.rangeQuery(M+1, R))