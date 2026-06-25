# https://neetcode.io/problems/is-anagram/history
# https://neetcode.io/problems/is-anagram/notes

## Solved in 55 min. using tips and solution

# Idea after read tips was to use two dict for two strings to save their characters frequency:
# check length: s.length != t.length - return false
# use two 'dict' to save frequency of each character from both strings by going in one loop
# then check: if frequencies are equal - return true, if not - return false

# confused how to implement to save them)
# so was need to check the solution -> https://neetcode.io/problems/is-anagram/solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0) # s = "abcadcc" - sCount['a'] = 1 + sCount.get('a', 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0) # t = "ccadcba" - sCount['c'] = 1 + sCount.get('c', 0)

        return sCount == tCount
        
