class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_water = 0
        while left < right:
            cur_water = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, cur_water)
            if heights[right] >= heights[left]:
                left += 1
            else:
                right -= 1
        return max_water