"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

"""

def alphabet_position(text):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = alphabets.lower()
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