# s = 'Was it a cat i saw?'
# s = 'second test'
s = 'A man, a plan, a canal: Panama'


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


def is_palindrome_2(s):
    i, j = 0, len(s)-1

    while i < j:
        while not is_alpha(s[i]) and i < j:
            i += 1
        while not is_alpha(s[j]) and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
    return True


def is_alpha(s):
    return (ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9'))


# print(is_palindrome_2(s))
print(2 % 5)
