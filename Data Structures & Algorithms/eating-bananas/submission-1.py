'''
l = 1 and r = max(piles) = 4
m = 
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def eat_rate(m):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / m)
            return count
        
        while l <= r:
            m = (l + r) // 2
            if eat_rate(m) > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res

            
         
                    
