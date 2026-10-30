class Solution:
    def maxDepth(self, s: str) -> int:
        c, b = 0, 0 
        for char in s:
            if char == '(':
                c += 1
            elif char == ")":
                c -= 1
            b = max(b, c)
        return b