class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map = dict()

        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        for i in t:
            if i in hash_map:
                hash_map[i] -= 1
            else:
                hash_map[i] = 1

        for i in hash_map:
            if hash_map[i] != 0:
                return False

        return True


# Input: s = "anagram", t = "nagaram"
# Output: true
