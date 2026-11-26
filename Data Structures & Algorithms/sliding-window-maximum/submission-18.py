# Runtime Complexity: O(n log n)
# Space Complexity: O(n)

from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k or not nums:
            return []

        res = []
        heap = []

        for i in range(k):
            heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])

        for right in range(k, len(nums)):
            heappush(heap, (-nums[right], right))

            while heap[0][1] <= right - k:
                heappop(heap)
            res.append(-heap[0][0])

        return res
