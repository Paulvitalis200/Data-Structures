"""
Stack
Last in First Out

ABCDE

E
D
C
B
A

"""


class Stack:
    def __init__(self):
        self.items = []

    def get_stack(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []


my_stack = Stack()

my_stack.add_item('B')
my_stack.add_item('C')
print("MY STACK: ", my_stack.get_stack())
# my_stack.remove_item()
# print("STEST: ", my_stack.get_stack())
# print("IS EMPTY: ", my_stack.is_empty())
# print("LAsT ITEM: ", my_stack.peek())
