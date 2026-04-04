'''
[9,2,2,4,6,1,5]

[1,2,2,4,5,6,9] target = 6


'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(start, total):
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                #if total + candidates[i] > target:
                    #break

                path.append(candidates[i])

                dfs(i + 1, total + candidates[i])
                path.pop()

        dfs(0, 0)
        return res