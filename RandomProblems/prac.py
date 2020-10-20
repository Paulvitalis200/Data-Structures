input_str = "Pauldreamer"
vowels = "aeiou"

def len_string(input_str):
    if len(input_str) == 0:
        return 0
    return 1 + len_string(input_str[1:])

def count_consonants(input_str):
    if len(input_str) == 0:
        return 0
    if input_str[0] not in vowels:
        return 1 + count_consonants(input_str[1:])
    else:
        return count_consonants(input_str[1:])

print(count_consonants(input_str))