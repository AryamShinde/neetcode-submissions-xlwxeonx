'''
Need a way to add cars based on position in stack
Cars exit stack when they reach, multiple cars might exit at the same time,
Need to track how many cars exit together, so basically track when do cars leave 
(4,2) (1,2) (0,1) (7,1)
[]
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        
