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


llist = LinkedList()
llist.append('A')
llist.append('B')
# llist.prepend('C')

llist.insert_after_node(llist.head, 'D')
llist.print_list()
