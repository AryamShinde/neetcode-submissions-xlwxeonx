class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in newMap:
                return [newMap[diff], i]
            newMap[num] = i
            
                