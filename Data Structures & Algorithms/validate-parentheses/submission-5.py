class Solution:
    def isValid(self, s: str) -> bool:
        # Ключ — закрывающая скобка, значение — открывающая
        cDic = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in cDic:  # Если скобка закрывающая
                # Проверяем, совпадает ли она с последней открывающей в стеке
                if stack and stack[-1] == cDic[char]:
                    stack.pop()
                else:
                    return False
            else:  # Если скобка открывающая
                stack.append(char)

        # Если стек пустой — все скобки закрылись правильно
        return not stack
