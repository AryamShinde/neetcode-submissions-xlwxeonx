class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            area = width * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            max_area = max(max_area, area)
        return max_area