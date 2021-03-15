"""
Write an efficient function to return maximum occurring character in the
input string e.g., if input string is “test” then function should return ‘t’.
"""

def most_occurrence(input_str):
    ht = {}

    for i in input_str:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    val = max(ht, key=ht.get)
    
    return val

print('Most', most_occurrence('coimmmmorbidities'))