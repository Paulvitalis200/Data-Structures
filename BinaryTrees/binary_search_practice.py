class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                return self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                return self._insert(data, cur_node.right)
        else:
            print("Value already in tree")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)

            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data == cur_node.data:
            return True
        else:
            return False

    def print_tree(self):
        if self.root:
            return self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(str(cur_node.data))
            self._print_tree(cur_node.right)

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data < cur_node.left.data:
                return False
            else:
                return self._is_bst_satisfied(cur_node.left, cur_node.left.data)
        elif cur_node.right:
            if data > cur_node.right.data:
                return False
            else:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.data)


bst = BST()
bst.insert(39)
bst.insert(4)
bst.insert(73)
bst.insert(10)
bst.insert(20)
bst.insert(14)

print(bst.find(18))

bst.print_tree()

print(bst.is_bst_satisfied())
