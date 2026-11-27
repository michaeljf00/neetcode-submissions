# Runtime Complexity: O(n * log m)
# Space Conmplexity : O(1)

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_speed = right

        while left <= right:
            k = (left + right) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            if time <= h:
                min_speed = k
                right = k - 1
            else:
                left = k + 1

        return min_speed

