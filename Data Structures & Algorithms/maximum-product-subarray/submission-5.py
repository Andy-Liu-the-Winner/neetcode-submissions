class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            if n < 0:
                curMax, curMin = curMin, curMax
            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)
            res = max(res, curMax)
        return res