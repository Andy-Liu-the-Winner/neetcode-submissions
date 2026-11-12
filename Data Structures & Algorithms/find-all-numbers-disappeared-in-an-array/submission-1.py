class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {i:1 for i in range(1, n + 1)}
        res = []

        for e in nums:
            if e in d:
                d[e] = 0
        for k, e in d.items():
            if e != 0:
                res.append(k)

        return res