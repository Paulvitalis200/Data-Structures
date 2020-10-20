"""
Given some integer, n. Determine the nth term in
the "look-and-say" sequence.

Example:

For n = 4, the 4th term in the sequence is 1211.

"""

def next_number(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


s = "1"
n = 6
for i in range(n-1):
    s = next_number(s)
    print(s)
# s = "1211"
# print(next_number(s))
