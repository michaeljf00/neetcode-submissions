# Runtime Complexity: O(n)
# Space Compelexity: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        freqs1 = [0] * 26
        freqs2 = [0] * 26
        for i in range(len(s1)):
            freqs1[ord(s1[i]) - ord('a')] += 1
            freqs2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if freqs1[i] == freqs2[i]:
                matches += 1
        
        for i in range(len(s2) - len(s1)):
            if matches == 26:
                return True
            
            c1 = s2[i]
            index1 = ord(c1) - ord('a')
            freqs2[index1] -= 1
            if freqs1[index1] == freqs2[index1]:
                matches += 1
            elif freqs1[index1] - 1 == freqs2[index1]:
                matches -= 1

            c2 = s2[i+len(s1)]
            index2 = ord(c2) - ord('a')
            freqs2[index2] += 1
            if freqs1[index2] == freqs2[index2]:
                matches += 1
            elif freqs1[index2] + 1 == freqs2[index2]:
                matches -= 1
            
        return matches == 26