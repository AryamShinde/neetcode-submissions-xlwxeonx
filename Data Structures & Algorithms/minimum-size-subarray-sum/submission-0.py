class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float('inf')
        s = 0
        
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                length = (r - l) + 1
                min_len = min(min_len, length)
                s -= nums[l]
                l += 1
                
           
        return 0 if min_len == float('inf') else min_len
            
            
