# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s):
    window = set()
    L = 0
    length = 0

    for R in range(len(s)):
        while s[R] in window:
            window.remove(s[L])
            L += 1
        length = max(R-L+1, length)
        window.add(s[R])
    
    return length

print(lengthOfLongestSubstring("abcabcbb"))