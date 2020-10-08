s =  "Was it a cat I saw?"
s = "Tenet"

#  Solutionn uses extra space proportional to size of string "s"
# s = f

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

print(is_palindrome(s))

# Steps
# Move through the string from the left 
# Check whether item is not alpha numeric and move forward if it is
# Move through the string from the right
# Check whether item is not alpha numeric and move forward if it is
# Check if the items in lowercase on the left match those on the right