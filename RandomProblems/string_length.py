# Given a string, calculate the length of the string

input_str = "LucidProgramming"

print(len(input_str))

def iterative_str_len(input_str):
    count = 0
    while 0 < len(input_str):
        count += 1
        input_str = input_str[:-1]
    return count

def iterative_two(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

"""
Every time we coode a recursive fucntion, we think of two things.
1. What is the base case
2. What are the recursive calls. The calls to the function itself that makes the function smaller
On every call to the func we need to get close to the base case
"""
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

print(iterative_str_len(input_str))
print(iterative_two(input_str))
print(recursive_str_len(input_str))