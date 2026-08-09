class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        sum_list = [nums[0]]
        for i in range(1, l):
            sum_list.append(nums[i] + sum_list[i - 1])

        # construct running minimum prefix
        running_min = [0] * l
        running_min[0] = 0
        for i in range(1, l):
            running_min[i] = min(running_min[i - 1], sum_list[i - 1])

        ans = nums[0]
        for i in range(l):
            ans = max(ans, sum_list[i] - running_min[i])

        return ans