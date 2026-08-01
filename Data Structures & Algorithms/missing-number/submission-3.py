class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (len(nums)) * (len(nums) + 1)// 2 # would be gaurentee to be an int
        for e in nums:
            sum -= e
        return sum 
