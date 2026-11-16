# Runtime Complexity: O(n)
# Space Complexity: O(m)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        window = {}

        max_window = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_reps = max(window.values())

            while right - left + 1 - max_reps > k:
                window[s[left]] -= 1
                left += 1
            
            max_window = max(max_window, right - left + 1)

        return max_window
            
                


            

            
