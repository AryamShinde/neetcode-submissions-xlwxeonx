class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)

        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)

        return res
