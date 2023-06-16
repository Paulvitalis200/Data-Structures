# Determine if a path exists from  the  root  of the  tree to  a leaf node.  It may not contain zeros
# Test

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def canReachLeaf(self, root):
        if not root or root.val == 0:
            return False

        if not root.left and not root.right:
            return True
        if self.canReachLeaf(root.left):
            return True
        if self.canReachLeaf(root.right):
            return True
        return False

    def leafPath(self, root, path):
        if not root or root.val == 0:
            return False
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if self.leafPath(root.left, path):
            return True
        if self.leafPath(root.right, path):
            return True
        path.pop()
        return False
