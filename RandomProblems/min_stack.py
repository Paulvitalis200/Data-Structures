class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if self.min_stack:
            item = min(self.min_stack[-1], self.stack[-1])
        self.min_stack.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.min_stack[-1]


stack = Stack()
stack.push(20)
stack.push(10)
stack.push(3)
stack.push(20)
stack.push(32)

print(stack.getMin())
