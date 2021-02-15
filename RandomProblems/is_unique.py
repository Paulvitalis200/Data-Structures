"""
Implement an algorithm to determine if a string has all unique characters.
"""

unique_string = "AbcDefG"
non_unique_string = "non Unique STR"


def is_unique(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    ht = dict()

    for i in input_str:
        if i in ht:
            print("We got one!")
            return False
        else:
            ht[i] = 1
    return True



# Space complexity: O(1)
def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)

def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    input_str = input_str.lower()
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

print(is_unique(unique_string))
print(is_unique(non_unique_string))

print(is_unique_2(unique_string))
print(is_unique_2(non_unique_string))

print(is_unique_3(unique_string))
print(is_unique_3(non_unique_string))