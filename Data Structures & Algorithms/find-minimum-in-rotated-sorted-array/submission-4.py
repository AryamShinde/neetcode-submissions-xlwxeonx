'''
[3,4,5,6,1,2]
       l
       r 
         m      
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 1000
        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:             
                r = m - 1
        return res