# Runtime Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0] * len(height), [0] * len(height)
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            maxRight[len(height)-i-1] = max(maxRight[len(height)-i], height[len(height)-i])
        
        total = 0
        for i in range(len(height)):
            total += max(0, min(maxRight[i], maxLeft[i]) - height[i])

        return total
        

            