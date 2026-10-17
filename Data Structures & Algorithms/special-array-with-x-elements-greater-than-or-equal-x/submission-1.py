class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (n + 1) # 0->n
        
        for num in nums:
            count[min(num, n)] += 1
        total = 0

        for x in range(n, 0, -1):
            total += count[x]
            if total == x:
                return x 
        return -1
