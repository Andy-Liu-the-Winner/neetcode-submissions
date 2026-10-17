class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums)) 
        nums.sort()
        increasing = True
        ptr = 0 
        n = len(nums)
        m = 1
        curr = 1
        while ptr < n - 1:
            if not nums[ptr] - nums[ptr + 1] == -1:
                m = max(curr, m)
                curr = 1
            else:
                m = max(curr, m)
                curr += 1
            ptr += 1
        m = max(curr, m)
        return m