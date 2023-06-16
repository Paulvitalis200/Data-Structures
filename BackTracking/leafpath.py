
def leafpath(root, path):
    if root is None or root.val == 0:
        return False

    path.append(root.val)

    if not root.left and not root.right:
        return False
    if leafpath(root.left, path):
        return True
    if leafpath(root.right, path):
        return True

    path.pop()
    return False
