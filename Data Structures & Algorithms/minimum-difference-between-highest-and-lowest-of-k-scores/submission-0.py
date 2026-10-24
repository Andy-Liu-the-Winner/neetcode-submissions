class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        m = float("inf")
        for i in range(0, len(nums) - k + 1):
            a, b = nums[i], nums[i + k - 1]
            m = min(m, b - a)
        return m