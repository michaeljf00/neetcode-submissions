class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        chars_s1 = {}
        chars_s2 = {}
        window_len = len(s1)

        for i in range(len(s1)):
            chars_s1[s1[i]] = chars_s1.get(s1[i], 0) + 1
            chars_s2[s2[i]] = chars_s2.get(s2[i], 0) + 1


        for i in range(window_len, len(s2)):
            if chars_s1 == chars_s2:
                return True
            chars_s2[s2[i-window_len]] -= 1
            if chars_s2[s2[i-window_len]] == 0:
                del chars_s2[s2[i-window_len]]

            chars_s2[s2[i]] = chars_s2.get(s2[i], 0) + 1

        return chars_s1 == chars_s2


        