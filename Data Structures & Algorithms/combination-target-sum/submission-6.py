'''
[2,5,6,9]

'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = [] # []
        path = [] # [2, 2, 2, 2]

        def dfs(start, total): #(0, 8)
            if total == target: # 8 != 9
                res.append(path.copy())
                return

            if total > target: # 8 !> 9
                return
            
            for i in range(start, len(nums)):
                if total + nums[i] > target: # 8 + 2 > 9
                    break

                path.append(nums[i])
                dfs(i, total + nums[i])
                path.pop()

        dfs(0, 0)
        return res

        