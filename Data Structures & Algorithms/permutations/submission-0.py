'''
[1,2,3]
[1,2,3] len = len og num


'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                path.append(nums[i])
                used.add(i)

                backtrack()

                path.pop()
                used.remove(i)

        backtrack()
        return result
