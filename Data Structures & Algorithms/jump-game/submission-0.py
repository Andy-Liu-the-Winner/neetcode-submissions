class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for j in range(nums[i] + 1):
                    if j + i >= len(nums): break
                    dp[j + i] = True
        return dp[-1]
