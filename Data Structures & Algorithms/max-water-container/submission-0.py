class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l != r:
            left, right = heights[l], heights[r]
            res = max(res,(r - l) * min(left, right))
            if left < right:
                l += 1
            else:
                r -= 1
            
        return res
