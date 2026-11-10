# Runtime Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            summed_val = numbers[left] + numbers[right]
            if summed_val < target:
                left += 1
            elif summed_val > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        return [-1, -1]
