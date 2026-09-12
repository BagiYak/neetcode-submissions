class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for t in tokens:
            if t == "+":
                second = stack.pop()
                first = stack.pop()
                result = first + second
                stack.append(result)
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                result = first - second
                stack.append(result)
            elif t == "*":
                second = stack.pop()
                first = stack.pop()
                result = first * second
                stack.append(result)
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                result = int(first / second)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[-1]