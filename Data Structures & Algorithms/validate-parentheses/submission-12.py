# Runtime Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = { '}': '{', ')': '(', ']':'['}

        stack = []

        for c in s:
            if c in parentheses:
                if not stack or stack.pop() != parentheses[c]:
                    return False
            else:
                stack.append(c)

        return not stack
            
            