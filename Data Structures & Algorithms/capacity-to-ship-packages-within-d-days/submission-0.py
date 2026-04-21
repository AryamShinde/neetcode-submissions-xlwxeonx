class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def weight_calc(cap):
            days_used = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w <= cap:
                    curr_weight += w
                else:
                    days_used += 1
                    curr_weight = w
            return days_used



        while l <= r:
            m = (l + r) // 2

            if weight_calc(m) <= days:
                r = m - 1
            else:
                l = m + 1
        return l
