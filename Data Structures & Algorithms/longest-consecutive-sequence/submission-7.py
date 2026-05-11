class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        if not nums:
            return 0

        max_len = 0

        for num in numSet:
            length = 1
            while num + 1 in numSet:
                num += 1
                length += 1
            
            max_len = max(max_len, length)

        return max_len