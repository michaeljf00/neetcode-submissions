
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        chars_s1 = {}
        chars_s2 = {}

        for i in range(len(s1)):
            chars_s1[s1[i]] = chars_s1.get(s1[i], 0) + 1
            chars_s2[s2[i]] = chars_s2.get(s2[i], 0) + 1

        matches = 0

        for c in chars_s1:
            if chars_s1[c] == chars_s2.get(c, 0):
                matches += 1

        required = len(chars_s1)


        for i in range(len(s1), len(s2)):
            if matches == required:
                return True

            # Add incoming character
            c = s2[i]
            if c in chars_s1:
                if chars_s2.get(c, 0) == chars_s1[c]:
                    matches -= 1
                chars_s2[c] = chars_s2.get(c, 0) + 1
                if chars_s2[c] == chars_s1[c]:
                    matches += 1
            else:
                chars_s2[c] = chars_s2.get(c, 0) + 1

            # Remove outgoing character
            c2 = s2[i - len(s1)]
            if c2 in chars_s1:
                if chars_s2[c2] == chars_s1[c2]:
                    matches -= 1
                chars_s2[c2] -= 1
                if chars_s2[c2] == chars_s1[c2]:
                    matches += 1
            else:
                chars_s2[c2] -= 1

        return matches == required
