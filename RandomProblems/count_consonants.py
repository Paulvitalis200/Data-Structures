# Given a string, count the number of consonants.
# Notee a consonant is a letter that is not a vowel,
# i.e. a letter that is not a, e, i, o, or u.

input_str_1 = "abc de"
input_str_2 = "LuCiDProGrramMiNG"

vowels = "aeiou"

def count_consonants(input_str):
    consonant_count = 0
    for i in input_str.lower():
        if i not in vowels:
            consonant_count += 1
    return consonant_count

def count_consonants_recursive(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + count_consonants_recursive(input_str[1:]) 
    else:
        return count_consonants_recursive(input_str[1:])