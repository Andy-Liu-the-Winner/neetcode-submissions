class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) // 3
        res = []
        c = Counter(nums)
        for k, v in c.items():
            if v > l:
                res.append(k)
        return res