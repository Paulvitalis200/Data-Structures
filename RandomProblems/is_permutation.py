"""
Given two strings, write a method to decide 
if one is a permuation  of the other.
"""

is_permutation_1 = "god"
is_permutation_2 = "dog"

not_permutation_1 = "not"
not_permutation_2 = "top"


# Time complexity: O(n log n)
# Space complexity: O(1)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        print("Not a permutation")
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True

# Time complexity: O(n)
# Space complexity: O(n)
def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        print("Not a permutation")
        return False

    ht = dict()
    for i in str_1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in str_2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False

    return True



print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print("------------------------------")
print("Hash Table implementation")
print("------------------------------")
print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))