class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (nums[-1] + 1) * len(nums) // 2 # would be gaurentee to be an int
        for e in nums:
            sum -= e
        return sum 
