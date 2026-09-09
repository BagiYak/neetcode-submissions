class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack = []
        for c in s:
            if c in parentheses:
                if stack and parentheses[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        
        return not stack
