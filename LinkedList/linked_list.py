class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        # Create node for the item we want to prepend
        new_node = Node(data)

        #  Set the  head as the new node's next value
        new_node.next = self.head
        # Reassign the head to be the new node that we want
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        # Check if the previous node is in the Linked List
        if not prev_node:
            print('Previous node not in Linked List')

        # Keep track of the node we want to add
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    
    '''
    Delete node
    
    Given a key (data field) delete node with this field
    Assume elements in linked list are unique

    Example: Delete node with data field "B"

    Two cases:
    - Node to be deleted is head
    - Node to be deleted is not head
    '''

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    '''
    Delete node at position
    Given a position, delete node with this position.

    Assume elements in linked list are unique

    Example: Delete node with position 1
    '''

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    '''
    Calculating length of list
    '''
    def len_iterative(self):
        count =  0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.prepend('C')

# llist.insert_after_node(llist.head, 'D')

# llist.delete_node_at_pos(1)

# print(llist.len_iterative())
print(llist.len_recursive(llist.head))
# llist.print_list()
