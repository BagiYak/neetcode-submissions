class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        for c in s:
            if c in dic:
                if stack and dic[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False