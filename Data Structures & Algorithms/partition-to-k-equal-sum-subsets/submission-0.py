class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        sums = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if sums[j] + nums[i] > target:
                    continue
                if j > 0 and sums[j] == sums[j - 1]:
                    continue

                sums[j] += nums[i]
                if dfs(i + 1):
                    return True

                sums[j] -= nums[i]

            return False

        return dfs(0)