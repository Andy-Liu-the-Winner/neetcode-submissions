class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        curr = 0
        dp = [defaultdict(int) for i in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                res += count
                dp[i][diff] += count + 1

        return res