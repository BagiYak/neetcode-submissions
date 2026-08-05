class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letters_1 = [0] * 26
        letters_2 = [0] * 26
        for i in range(len(s)):
            index_1 = ord(s[i]) - ord('a')
            index_2 = ord(t[i]) - ord('a')
            letters_1[index_1] += 1
            letters_2[index_2] += 1

        return letters_1 == letters_2