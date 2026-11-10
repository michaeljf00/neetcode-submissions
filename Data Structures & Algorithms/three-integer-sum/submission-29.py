# Runtime Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            left = i+1
            right = len(sorted_nums)-1
            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left+1]:
                        left += 1
                    left += 1

        return res

                
