class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in new_map:
                return [new_map[diff], i]
            new_map[n] = i