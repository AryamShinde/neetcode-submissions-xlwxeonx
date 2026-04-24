class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                curr.append(nums[i])
                used[i] = True
                dfs(curr, used)
                curr.pop()
                used[i] = False


        dfs([], [False] * len(nums))
        return res
                