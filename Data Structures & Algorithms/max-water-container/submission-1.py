class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            max_area = max(max_area, area)
        return max_area