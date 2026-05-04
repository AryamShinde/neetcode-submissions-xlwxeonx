class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in new_map:
                return [new_map[diff], i]
            new_map[num] = i
            
                