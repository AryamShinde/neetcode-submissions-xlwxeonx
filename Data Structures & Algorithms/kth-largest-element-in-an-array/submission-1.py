class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while len(nums) + 1 > k:
            res = nums[0]
            heapq.heappop(nums)

        return res
