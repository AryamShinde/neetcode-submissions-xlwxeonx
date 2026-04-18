class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        prefixSums = {0 : 1}

        for num in nums:
            curr += num
            diff = curr - k

            res += prefixSums.get(diff, 0)
            prefixSums[curr] = 1 + prefixSums.get(curr, 0)

        return res