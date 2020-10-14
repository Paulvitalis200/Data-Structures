# Given a string, find the first uppercase character/
# Solve using both an iterative and recursive solution.

input_str_1 = "lucidProgramming"
input_str_2 = "LucidZrogramming"
input_str_3 = "lucidprogramming"

def find_uppercase_iterative(input_str):
    # Loop through every character and check if the character we are on
    # is uppercase. If not we continue
    for i in range(len(input_str)):
        if input_str[i].isupper():      
            return input_str[i]
    return "No uppercase character found"

# When doing a recursive approach, we need to constantly
# move down the problem. We can set an index
# which tells us where to start and as we process the string
# recursively we increment the index
def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, idx+1)


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))