class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #[1,2,+,3,3,*,9]

        for i in tokens:
            a = 0
            b = 0
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "*":
                stack.append(a * b)
            elif i == "-":
                stack.append(b - a)
            elif i == "/":
                stack.append(int(b / a))
            else:
                stack.append(int(i))
            print(stack)
        return stack[-1]