class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        t_chars = {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        window_chars= {}
        required = len(t_chars)
        matches = 0

        left = 0
        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            c = s[right]

            if c in t_chars:
                window_chars[c] = window_chars.get(c, 0) + 1

                if window_chars[c] == t_chars[c]:
                    matches += 1

            while matches == required:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_char = s[left]

                if left_char in t_chars:
                    if window_chars[left_char] == t_chars[left_char]:
                        matches -= 1

                    window_chars[left_char] -= 1

                left += 1
            
        return s[best_start:best_start+best_len] if best_len != float("inf") else ""

