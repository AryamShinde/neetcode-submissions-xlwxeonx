class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        if not nums:
            return 0

        max_len = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                length = 1

                while curr + 1 in numSet:
                    curr += 1
                    length += 1
            
                max_len = max(max_len, length)

        return max_len