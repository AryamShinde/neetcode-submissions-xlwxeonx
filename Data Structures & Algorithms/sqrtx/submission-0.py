class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:# 0,1,2,3,4,5,6,7,8,9,10,11,12,13
            m = (l + r) // 2

            if (m * m) < x:
                l = m + 1
                res = m
            elif (m * m) > x:
                r = m - 1
            else:
                return m

        return res 