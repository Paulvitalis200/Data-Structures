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
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data > root.data:
            if root.right.data is None:
                root.right  = Node(data)
            else:
                self._insert(root.right, data)
        elif data < root.data:
            if  root.left.data is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            print("Value alreay in BST")

bst = BST()