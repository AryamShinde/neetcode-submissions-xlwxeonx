class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            dist = r - l
            area = min_height * dist
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)

        return max_area