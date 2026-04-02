'''
n = 3
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n #[-1, 2, 1]
        def dfs(i):
            if i >= n:# 3 >= 3 
                return i == n # 3 == 3, return True = 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2) # cache[0] = dfs(1) + dfs(2) = 2 + 1 = 3
            return cache[i]

        return dfs(0)

        