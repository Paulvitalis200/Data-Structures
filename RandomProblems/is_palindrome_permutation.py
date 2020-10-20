"""
Given a string, write a functionn to check if it is 
a permutation of a palindrome. A palindrome is a word
or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just
dictionary words.

e.g
racecar
acecarr
"""

palin_perm = "Tact Coa"
not_palin_perm  = "This is not a palindrome permutation"
 
 # Time Complexity: O(n)
 #  Space Complexity: O(n)
def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    ht = dict()

    for i in input_str:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    odd_count = 0
    for k, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
        
    return True

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))