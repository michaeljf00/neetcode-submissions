# Runtime Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        hashed_set = set(nums)

        for n in hashed_set:
            i = 1
            while not n-1 in hashed_set and n+i in hashed_set:
                i += 1
            max_length = max(max_length, i)

        return max_length