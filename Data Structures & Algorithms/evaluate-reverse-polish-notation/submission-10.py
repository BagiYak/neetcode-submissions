class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        result = 0
        for c in tokens:
            if c == '+':
                # print(f"Add = {c}")
                second = stack.pop()
                first = stack.pop()
                result = first + second
                stack.append(int(result))
                # print(f"Add result = {first} {c} {second} = {stack[-1]}")
            elif c == '-':
                # print(f"Remove = {c}")
                second = stack.pop()
                first = stack.pop()
                result = first - second
                stack.append(int(result))
                # print(f"Remove result = {first} {c} {second} = {stack[-1]}")
            elif c == '*':
                # print(f"Multiply = {c}")
                second = stack.pop()
                first = stack.pop()
                result = first * second
                stack.append(int(result))
                # print(f"Multiply result = {first} {c} {second} = {stack[-1]}")
            elif c == '/':
                # print(f"Divide = {c}")
                second = stack.pop()
                first = stack.pop()
                result = first / second
                stack.append(int(result))
                # print(f"Divide result = {first} {c} {second} = {stack[-1]}")
            else:
                # print(f"ELSE = {c}")
                stack.append(int(c))
                # print(f"Append result = {stack[-1]}")

        return int(result)