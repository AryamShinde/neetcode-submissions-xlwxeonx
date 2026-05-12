class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        if not nums:
            return 0

        max_length = 0

        for n in nums:
            length = 1
            if n - 1 in numSet:
                continue

            while n + 1 in numSet:
                length += 1
                n += 1

            max_length = max(max_length, length)

        return max_length

            

