"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

"""

# Time complexity: O(n)^2

"""
Methodology
1. Define string of alphabets and an empty hashtable.
2. Loop through the alphabets and place them in the hashtable with their
corresponding number on the alphabet.
3. Convert text to lowercase.
4. For each letter, if its in the hash table, push it onto a new string.
5. Return the new string.
"""

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# def alphabet_position(text):
#     if type(text) == str:
#         text = text.lower()
#         result = ''
#         for letter in text:
#             if letter.isalpha() == True:
#                 result = result + ' ' + str(alphabet.index(letter) + 1)
#         return result.lstrip(' ')

def alphabet_position(text):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    ht = dict()
    i = 0
    while i < len(alphabets):
        if i == 0:
            ht[1] = alphabets[i]
            i+=1
        else:
            ht[i+1] = alphabets[i]
            i += 1
    
    final_string = ''
    for j in text.lower():
        for key, value in ht.items():
            if j == value:
                final_string += str(key) + ' '
    last_character = len(final_string)-1
    final = final_string[0:last_character]
    return final
    
print(alphabet_position("The sunset sets at twelve o' clock."))