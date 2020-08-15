class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def reverse_string(stack, input_str):
    # Loop through  the string and push contents
    # character by character onto stack

    for i in  range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str

s = Stack()
# s.push("A")
# s.push("B")
# print(s.get_stack())
# s.push("C")
# s.push("D")
# s.push("E")
# print(s.get_stack())
# s.pop()

# print(s.get_stack())
# print(s.is_empty())
# print(s.peek())
input_str  = 'Paulski'
print(reverse_string(s, input_str))
