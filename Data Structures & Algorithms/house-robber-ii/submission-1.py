class Solution:
    def rob(self, nums: List[int]) -> int:
        # main idea: max(rob nums[0: n - 1], rob nums[1: n])
        n = len(nums)
        if n == 1: return nums[0]
        def helper(nums):
            n = len(nums)
            if not n: return 0
            dp = [0 for i in range(n)] # dp[i]: max we rob before ith index
            dp[0] = nums[0]
            for i in range(1, n):
                # compare sol with no curr and curr
                prev = dp[i - 1] # has no curr
                curr = dp[i - 2] + nums[i] if i > 1 else nums[i]
                dp[i] = max(prev, curr)
            print(dp)
            return dp[-1]
        rob1 = helper(nums[0: n - 1])
        rob2 = helper(nums[1: n])
        return max(rob1, rob2)
