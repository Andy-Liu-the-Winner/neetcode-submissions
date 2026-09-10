class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        d = {}
        res = []

        for e in nums:
            d[e] = d.get(e , 0) + 1
        
        for e in d:
            if d[e] > n:
                res.append(e)
        return res