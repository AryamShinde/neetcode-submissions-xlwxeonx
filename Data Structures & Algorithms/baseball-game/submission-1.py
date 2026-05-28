class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "C":
                stack.remove(stack[-1])
            else:
                stack.append(int(i))
        print(stack)
            
        return sum(stack)