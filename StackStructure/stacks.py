"""
Stack Data Structure
D
C
B
A

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


books = Stack()
books.push('A')
books.push('B')
print(books.get_stack())
books.push('C')
print("-------")
print(books.get_stack())
books.pop()
print("-------")
print(books.peek())
print(books.get_stack())
