"""
Implement an algorithm to determine if a string has all
unique characters.
"""

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

def normalize(input_str):
    input_string = input_str.replace(" ", "")
    return input_string.lower()

# Time complexity: O(n) - linear
# Space complexity: O(n) - linear We make use of an extra data structure
def is_unique_1(input_str):
    ht = dict()
    input_string = normalize(input_str)
    for i in input_string:
        if i in ht:
            return False
        else:
            ht[i] = 1
    return True

# Using sets. A set would return all unique characters on a string
# Space complexity: O(1)
# Time complexity: O(1)
def is_unique_3(input_str):
    return len(set(input_str)) == len(input_str)

def is_unique_4(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    input_str = normalize(input_str)
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

print(is_unique_1(unique_str))
# print(is_unique_2(non_unique_str))
print(is_unique_3(unique_str))
print(is_unique_4(unique_str))