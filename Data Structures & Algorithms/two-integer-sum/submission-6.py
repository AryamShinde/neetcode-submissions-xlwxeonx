class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in new:
                return [new[diff], i]
            new[n] = i