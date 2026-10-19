class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            ops = 0
            for x in nums:
                ops += (x - 1) // mid
            if ops <= maxOperations:
                r = mid 
            else:
                l = mid + 1
        return l
