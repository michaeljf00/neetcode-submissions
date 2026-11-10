# Runtime Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                maxArea = max(maxArea, heights[left] * (right - left))
                left += 1
            else:
                maxArea = max(maxArea, heights[right] * (right - left))
                right -= 1

        return maxArea