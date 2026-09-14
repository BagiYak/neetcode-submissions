# was a saw -> wasasaw - palinfrome can have odd numbers as well as even

class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanumeric = ''

        for c in s:
            if c.isalnum():
                alphanumeric += c.lower()
        
        l = 0
        r = len(alphanumeric) - 1
        middle = len(alphanumeric) // 2
        while l < middle:
            if alphanumeric[l] != alphanumeric[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True