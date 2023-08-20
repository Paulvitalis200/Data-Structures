# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.You are given a 
# string s and an integer k. You can choose any character 
# of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter
# you can get after performing the above operations.

def characterReplacement(s, k):
    count = {}
    res = 0
    L = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)  # if character doesn't exist return a default value of 0

        maxf = max(maxf, count[s[r]]) # set maxf equal to max off maxf or the count of the item we are trying to add

        # while (r-L+1) - max(count.values()) > k: we use maxf so that we don't have to loop over entire count  hashmap
        while (r-L+1) - maxf > k:
            count[s[L]] -= 1
            L += 1
        res = max(res, r-L+1)

    return res


print(characterReplacement("ABAB", 2))