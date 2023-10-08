class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# Time and space complexity: O(n)
def inorder(root):
    stack = []
    curr = root
    
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right

# Time and space complexity: O(n)
def preorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()

# Time and space complexity: O(n)
def postorder(root):
    stack = [root]
    visited = [False]

    while stack:
        curr, visited = stack.pop(), visited.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)