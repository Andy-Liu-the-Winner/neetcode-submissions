class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            n = nums[i]
            if n not in d:
                d[n] = i
        
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in d:
                index = d[diff]
                return [i, d[diff]]
            

