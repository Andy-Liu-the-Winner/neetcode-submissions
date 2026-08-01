class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import copy 
        d = {}
        ans = set()
        for e in nums:
            d[e] = d.get(e, 0) + 1
        def two_sum(sum, dict) -> List[tuple[int, int]]:
            # sum is the negative third number
            res = []
            for key in dict:
                dict[key] -= 1
                remaining = sum - key 
                if remaining in dict and dict[remaining] != 0:
                    res.append((key, remaining))
                dict[key] += 1
            return res
        
        for e in nums:
            dict = copy.deepcopy(d)
            dict[e] -= 1
            if dict[e] == 0:
                del dict[e]
            two_sum_list = two_sum(-e, dict)
            for (a, b) in two_sum_list:
                ans.add(tuple(sorted((e, a, b))))
        return [list(t) for t in ans]