def isValid(input_str):
    stack = []
    is_balanced = True
    for i in input_str:
        if i in "({[":
            stack.append(i)
        else:
            if len(stack) == 0:
                is_balanced = False
            else:
                top = stack.pop()
                if not isMatch(top, i):
                    is_balanced = False
    
    if is_balanced and len(stack) == 0:
        return True
    return False

def isMatch(s1, s2):
    if s1 == '{' and s2 == '}':
        return True
    elif  s1 == '['  and s2 == ']':
        return True
    elif  s1 == '(' and s2 == ')':
        return True
    else:
        return False
    
print(isValid("[][()]{}"))

