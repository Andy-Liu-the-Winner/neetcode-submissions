class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)

        def test(i, j, k):
            if nums[i] == nums[j]:
                dp[k] = True   
            if not k == len(nums):
                if nums[i] == nums[j] == nums[k] or nums[i] + 1 == nums[j] == nums[k] - 1:
                    dp[k + 1] = True

        test(0, 1, 2)
        
        for i in range(2, len(nums) - 1):
            if dp[i]:
                test(i, i + 1, i + 2)
        return dp[-1]


