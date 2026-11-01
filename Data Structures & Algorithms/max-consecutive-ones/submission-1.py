class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)
        return res