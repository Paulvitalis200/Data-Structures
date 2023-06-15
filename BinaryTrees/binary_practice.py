class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal):
        if traversal == 'preorder':
            return self.pre_order_print(tree.root, "")
        elif traversal == 'inorder':
            return self.in_order_print(tree.root, "")
        elif traversal == 'postorder':
            return self.post_order_print(tree.root, "")

    def pre_order_print(self,  start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        # Left -> Right  -> Root
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal = self.in_order_print(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.left.right = Node(3)
tree.root.right = Node(4)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)
tree.root.left.left = Node(7)


print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
