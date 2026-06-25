# cases:
# check length: s.length != t.length - return false
# use two 'dict' to save frequency of each character from both strings by going in one loop
# then check: if frequencies are equal - return true, if not - return false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0) # s = "abcadcc" - sCount['a'] = 1 + sCount.get('a', 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0) # t = "ccadcba" - sCount['c'] = 1 + sCount.get('c', 0)

        return sCount == tCount
        