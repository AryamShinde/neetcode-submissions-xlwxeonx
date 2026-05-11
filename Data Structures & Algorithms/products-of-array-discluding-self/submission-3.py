class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for n in nums[1:]:
            prod *= n
        res.append(prod)
        print(res)

        k = 1
        while k < len(nums):
            prod = 1
            for n in nums[:k] + nums[k + 1:]:
                prod *= n    
            res.append(prod)
            #prod = 1
            k += 1

        return res

        

            
